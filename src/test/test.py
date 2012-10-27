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

"""Test the module.
"""
import os
import sys
from subprocess import call
import time
import sqlite3

def run(model, f_names, build, pickle, check, solve, psolve, tmlim, memlim,
        preduce, D, debug):
    """Run test.
    
    :param model: model type.
    
    :type model: string.
    
    :param f_names: names of files.
    
    :type f_names: list.
    
    :param build: build data file from ppm.
    
    :type build: boolean.
    
    :param check: check model and data for error.

    type check: boolean.

    :param solve: try to solve the problem.

    :type solve: boolean.

    :param psolve: try to solve the problem using pickle file.

    :type psolve: boolean.

    :param tmlim: time limit.

    :type tmlim: integer.

    :param memlim: memory limit.

    :type memlim: integer.

    :param preduce: number of vertical and horizontal pixels to be reduce to
    one.

    :type preduce: integer.

    :param D: max distance between two points.

    :type D: float.

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
                f_max REAL,
                time REAL);
                """)
        con.commit()
    except:
        pass

    if not f_names:
        f_names = ['test/sample.ppm']
    for f in f_names:
        print('Processing {0}.'.format(f))
        if build:
            print('Reading {0}. This will take some time.'.format(f))
            if not model:
                test = aterro.Aterro(f, preduce, D)
            if model == 1:
                test = raterro.RAterro(f, preduce, D)
            if model == 2:
                test = aaterro.AAterro(f, preduce, D)
            print('Sucessfully read {0}.'.format(f))
            print('Writing data. This will take some time.')
            test.wdf()
            print('Sucessfully write data.')
        if pickle:
            print('Reading {0}. This will take some time.'.format(f))
            if not model:
                test = aterro.Aterro(f, preduce, D)
            if model == 1:
                test = raterro.RAterro(f, preduce, D)
            if model == 2:
                test = aaterro.AAterro(f, preduce, D)
            print('Sucessfully read {0}.'.format(f))
            print('Writing data. This will take some time.')
            test.wpf()
            print('Sucessfully write data.')
        if psolve:
            if not model:
                s = time.time()
                f_max = modelo.abs(f.replace('.ppm',
                    '{0}_aterro.pickle'.format(preduce)), tmlim * 1000,
                        memlim, True, False, debug)
                s = time.time() - s
                c.execute("""
                        INSERT INTO benchmark VALUES (
                        NULL,
                        datetime('now'),
                        'aterro',
                        ?,
                        'aterro',
                        ?,
                        ?)
                        """, (preduce, f_max, s))
                con.commit()
            if model == 1:
                s = time.time()
                f_max = modelo.rbs(f.replace('.ppm',
                    '{0}_raterro.pickle'.format(preduce)), tmlim * 1000,
                        memlim, True, False, debug)
                s = time.time() - s
                c.execute("""
                        INSERT INTO benchmark VALUES (
                        NULL,
                        datetime('now'),
                        'aterro com obstaculo',
                        ?,
                        'raterro',
                        ?,
                        ?)
                        """, (preduce, f_max, s))
                con.commit()
            if model == 2:
                s = time.time()
                f_max = modelo.rbs(f.replace('.ppm',
                    '{0}_aaterro.pickle'.format(preduce)), tmlim * 1000,
                        memlim, True, False, debug)
                s = time.time() - s
                c.execute("""
                        INSERT INTO benchmark VALUES (
                        NULL,
                        datetime('now'),
                        'aterro com obstaculo',
                        ?,
                        'aaterro',
                        ?,
                        ?)
                        """, (preduce, f_max, s))
                con.commit()
        if not model:
            m = 'aterro'
            f = f.replace('.ppm', '_aterro.ppm')
        if model == 1:
            m = 'raterro'
            f = f.replace('.ppm', '_raterro.ppm')
        if model == 2:
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
        $ python test/test.py -b 2 --pickle --psolve --preduce 100
    """

    import argparse

    # See functions at parent directory.
    parentdir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0,parentdir)

    # Parse of flags.
    parser = argparse.ArgumentParser(description='Test for MS480.')
    parser.add_argument('-b', type=int, default=0,
            help='using barrier in the model with contiuo space (1) or with discrete space (2).')
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
            args.debug)
