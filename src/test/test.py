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

def aterro(f_names, solve):
    """Test aterro.
    """
    import aterro

    if not f_names:
        f_names = ['test/sample12x12.ppm']
    for f in f_names:
        test = aterro.Aterro(f, 3)
        test.wdf()
        if solve:
            s = 'glpsol -m aterro.mod -d {0} -y {1} --log {2} \
            --tmlim 600 --memlim 512'.format(f.replace('.ppm', '_aterro.dat'),
            f.replace('.ppm', '_aterro.dis'), f.replace('.ppm', '_aterro.log'))
        else:
            s = 'glpsol -m aterro.mod -d {0} --log {1} --tmlim 600 \
                    --memlim 512 --check'.format(f.replace('.ppm',
                    '_aterro.dat'), f.replace('.ppm', '_aterro.log'))
        print(s)
        call(s, shell=True)

def raterro(f_names, solve):
    """Test raterro.
    """
    import raterro

    if not f_names:
        f_names = ['test/sample12x12.ppm']
    for f in f_names:
        test = raterro.RAterro(f, 3)
        test.wdf()
        if solve:
            s = 'glpsol -m raterro.mod -d {0} -y {1} --log {2} \
                    --tmlim 600 --memlim 512'.format(f.replace('.ppm',
                    '_raterro.dat'), f.replace('.ppm', '_raterro.dis'),
                    f.replace('.ppm', '_raterro.log'))
        else:
            s = 'glpsol -m raterro.mod -d {0} --log {1} --tmlim 600 \
                    --memlim 512 --check'.format(f.replace('.ppm',
                    '_raterro.dat'), f.replace('.ppm', '_raterro.log'))
        print(s)
        call(s, shell=True)

if __name__ == "__main__":
    parentdir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0,parentdir)

    f_names = sys.argv[1:]
    for i in xrange(f_names.count('solve')):
        f_names.remove('solve')
    for i in xrange(f_names.count('aterro')):
        f_names.remove('aterro')
    for i in xrange(f_names.count('raterro')):
        f_names.remove('raterro')
    if 'solve' in sys.argv[1:]:
        solve = True
    else:
        solve = False
    if 'aterro' in sys.argv[1:]:
        aterro(f_names, solve)
    if 'raterrp' in sys.argv[1:]:
        raterro(f_names, solve)
