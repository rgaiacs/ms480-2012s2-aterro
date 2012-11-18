# Copyright (c) 2012 Raniere Silva <r.gaia.cs@gmail.com>
# Copyright (c) 2012 Fernando Cezarino <feolce@gmail.com>
# Copyright (c) 2012 Ana Paula Diniz Marques <anapdinizm@gmail.com>
# Copyright (c) 2012 Camile Kunz <camileknz@gmail.com>
# Copyright (c) 2012 Ana Flavia <anaflavia.c.lima@gmail.com>
#
# This file is part of 'Experimentos Computacionais de MS480 - 2012S2 -
# Aterro com Obstaculo'.
#
# 'Experimentos Computacionais de MS480 - 2012S2 - Aterro com Obstaculo'
# is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
Test the module.
"""
import os
import sys
from subprocess import call
import time
import sqlite3

def run(model, f_names, build, pickle, check, solve, psolve, tmlim, memlim,
        preduce, D, dtype, debug):
    """Run test.
    
    :param model: model type and usefull information.
    
    :type model: list.
    
    :param f_names: names of files.
    
    :type f_names: list.
    
    :param build: build data file from ppm.
    
    :type build: boolean.
    
    :param check: check model and data for error.

    :type check: boolean.

    :param solve: try to solve the problem.

    :type solve: boolean.

    :param psolve: try to solve the problem using pickle file.

    :type psolve: boolean.

    :param tmlim: time limit.

    :type tmlim: integer.

    :param memlim: memory limit.

    :type memlim: integer.

    :param preduce: number of vertical and horizontal pixels to be reduce to one.

    :type preduce: integer.

    :param D: max distance between two points.

    :type D: float.

    :param dtype: type of distance.

    * ``0``: the distance between centers.
    * ``1``: the minimum distance.
    * ``2``: the maximum distance.

    :type dtype: integer

    :param debug: enable the debug behavior.

    :type debug: boolean.
    """
    import aterro
    import raterro
    import aaterro
    import modelo

    con = sqlite3.connect('test/test.db')
    c = con.cursor()
    try:
        c.executescript("""
                CREATE TABLE benchmark (
                id INTEGER PRIMARY KEY,
                date TEXT,
                problem TEXT,
                reduce INTEGER,
                solver TEXT,
                cols INTEGER,
                rows INTEGER,
                f_max REAL,
                p_time REAL,
                s_time REAL);
                """)
        con.commit()
    except:
        pass

    if not f_names:
        f_names = ['test/sample.ppm']
    for f in f_names:
        print(80*'-')
        print('Processing {0}.'.format(f))
        if build:
            print('Reading {0}. This will take some time.'.format(f))
            if not model:
                test = aterro.Aterro(f, preduce, D, dtype)
            elif model[0] == 1:
                test = raterro.RAterro(f, preduce, D, dtype)
            elif model[0] == 2:
                test = aaterro.AAterro(f, model[1:3], model[3], preduce, D,
                        dtype)
            print('Sucessfully read {0}.'.format(f))
            print('Writing data. This will take some time.')
            test.wdf()
            print('Sucessfully write data.')
        if pickle:
            print('Reading {0}. This will take some time.'.format(f))
            if not model:
                p_time = time.time()
                test = aterro.Aterro(f, preduce, D, dtype)
                p_time = time.time() - p_time
            elif model[0] == 1:
                p_time = time.time()
                test = raterro.RAterro(f, preduce, D, dtype)
                p_time = time.time() - p_time
            elif model[0] == 2:
                p_time = time.time()
                test = aaterro.AAterro(f, model[1:3], model[3], preduce, D, dtype)
                p_time = time.time() - p_time
            print('Sucessfully read {0}.'.format(f))
            print('Writing data. This will take some time.')
            test.wpf()
            print('Sucessfully write data.')
        if psolve:
            if not model:
                s_time = time.time()
                info = modelo.abs(f.replace('.ppm',
                    '_aterro_r{0}d{1}t{2}.pickle'.format(preduce, D, dtype)),
                    tmlim * 1000, memlim, True, False, debug)
                s_time = time.time() - s_time
                c.execute("""
                        INSERT INTO benchmark VALUES (
                        NULL,
                        datetime('now'),
                        ?,
                        ?,
                        'aterro',
                        ?,
                        ?,
                        ?,
                        ?,
                        ?)
                        """, (f, preduce, info['cols'], info['rows'], info['z'], p_time, s_time))
                con.commit()
            elif model[0] == 1:
                s_time = time.time()
                info = modelo.rbs(f.replace('.ppm',
                    '_raterro_r{0}d{1}t{2}.pickle'.format(preduce, D, dtype)),
                    tmlim * 1000, memlim, True, False, debug)
                s_time = time.time() - s_time
                c.execute("""
                        INSERT INTO benchmark VALUES (
                        NULL,
                        datetime('now'),
                        ?,
                        ?,
                        'raterro',
                        ?,
                        ?,
                        ?,
                        ?,
                        ?)
                        """, (f, preduce, info['cols'], info['rows'], info['z'], p_time, s_time))
                con.commit()
            elif model[0] == 2:
                s_time = time.time()
                info = modelo.rbs(f.replace('.ppm',
                    '_aaterro_r{0}d{1}t{2}.pickle'.format(preduce, D, dtype)),
                    tmlim * 1000, memlim, True, False, debug)
                s_time = time.time() - s_time
                c.execute("""
                        INSERT INTO benchmark VALUES (
                        NULL,
                        datetime('now'),
                        ?,
                        ?,
                        'aaterro',
                        ?,
                        ?,
                        ?,
                        ?,
                        ?)
                        """, (f, preduce, info['cols'], info['rows'], info['z'], p_time, s_time))
                con.commit()
        if not model:
            m = 'aterro'
            f = f.replace('.ppm', '_aterro.ppm')
        elif model[0] == 1:
            m = 'raterro'
            f = f.replace('.ppm', '_raterro.ppm')
        elif model[0] == 2:
            m = 'aaterro'
            f = f.replace('.ppm', '_aaterro.ppm')
        if check:
            s = 'glpsol -m {0}.mod -d {1} --log {2} --tmlim {3} '\
                    '--memlim {4} --check'.format(m, f.replace('.ppm',
                    '.dat'), f.replace('.ppm', '.log'), tmlim, memlim)
            print(s)
            call(s, shell=True)
        elif solve == True:
            s = 'glpsol -m {0}.mod -d {1} -y {2} --log {3} '\
                    '--tmlim {4} --memlim {5}'.format(m, 
                            f.replace('.ppm', '.dat'),
                            f.replace('.ppm', '.dis'),
                            f.replace('.ppm', '.log'),
                            tmlim, memlim)
            print(s)
            call(s, shell=True)
    con.close()


if __name__ == "__main__":
    """Call test from the command line interpreter. ::

        $ python test/test.py --pickle --psolve --preduce 100
        $ python test/test.py -b 1 --pickle --psolve --preduce 100
        $ python test/test.py -b 2 10 10 10 --pickle --psolve --preduce 100
    """
    import argparse

    # See functions at parent directory.
    parentdir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0,parentdir)

    # Parse of flags.
    parser = argparse.ArgumentParser(description='Test for MS480.')
    parser.add_argument('-b', nargs='*', type=int,
            help='using barrier in the model with discrete space (1) or with continuo space (2), with center and radium.')
    parser.add_argument('--data', action='store_true',
            help='build the data file based on ppm file. (deprecated)')
    parser.add_argument('--debug', action='store_true',
            help='enable the debug mode.')
    parser.add_argument('--pickle', action='store_true',
            help='build the data file, with pickle, based on ppm file.')
    parser.add_argument('--check', action='store_true',
            help='only check for error the problem. (deprecated)')
    parser.add_argument('--solve', action='store_true',
            help='solve the problem. (deprecated)')
    parser.add_argument('--psolve', action='store_true',
            help='solve the problem using pickle file.')
    parser.add_argument('--maxd', type=int, default=800,
            help='maxime distance between points that can be transporte.')
    parser.add_argument('--dtype', type=int, default=0,
            help="""type of distance.
                * ``0``: the distance between centers.
                * ``1``: the minimum distance.
                * ``2``: the maximum distance.""")
    parser.add_argument('--preduce', type=int, default=1,
            help='number of vertical and horizontal pixels to be reduce to one.')
    parser.add_argument('--tmlim', type=int, default=600,
            help='time limit (in seconds).')
    parser.add_argument('--memlim', type=int, default=512,
            help='memory limit (in megabits).')
    parser.add_argument('-f', nargs='*',
            help='name of ppm files to process')

    args = parser.parse_args()

    run(args.b, args.f, args.data, args.pickle, args.check, args.solve,
            args.psolve, args.tmlim, args.memlim, args.preduce, args.maxd,
            args.dtype, args.debug)
