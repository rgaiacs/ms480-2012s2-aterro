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

def run(model, f_names, build, check, solve):
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
    """
    import aterro
    import raterro

    if not f_names:
        f_names = ['test/sample12x12.ppm']
    for f in f_names:
        if build == True:
            print('Reading {0}. This will take some time.'.format(f))
            if model:
                test = raterro.RAterro(f, 8)
            else:
                test = aterro.Aterro(f, 8)
            print('Writing data. This will take some time.')
            test.wdf()
        if model:
            m = 'raterro'
            f = f.replace('.ppm', '_raterro.ppm')
        else:
            m = 'aterro'
            f = f.replace('.ppm', '_aterro.ppm')
        if check == True:
            s = 'glpsol -m {0}.mod -d {1} --log {2} --tmlim 3600 \
                    --memlim 4096 --check'.format(m, f.replace('.ppm',
                    '.dat'), f.replace('.ppm', '.log'))
            print(s)
            call(s, shell=True)
        elif solve == True:
            s = 'glpsol -m {0}.mod -d {1} -y {2} --log {3} \
            --tmlim 3600 --memlim 4096'.format(m, f.replace('.ppm', '.dat'),
            f.replace('.ppm', '.dis'), f.replace('.ppm', '.log'))
            print(s)
            call(s, shell=True)

if __name__ == "__main__":
    import argparse

    # See functions at parent directory.
    parentdir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0,parentdir)

    # Parse of flags.
    parser = argparse.ArgumentParser(description='Test for MS480.')
    parser.add_argument('-b', action='store_true',
            help='using barrier in the model.')
    parser.add_argument('--data', action='store_true',
            help='build the data file based on ppm file.')
    parser.add_argument('--check', action='store_true',
            help='only check for error the problem.')
    parser.add_argument('--solve', action='store_true',
            help='solve the problem.')
    parser.add_argument('-f', nargs='*',
            help='name of ppm files to process')

    args = parser.parse_args()

    run(args.b, args.f, args.data, args.check, args.solve)
