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

def aterro():
    """Test aterro.
    """
    import aterro

    test = aterro.Aterro('test/sample12x12.ppm', 3)
    test.wdf()

def raterro():
    """Test raterro.
    """
    import raterro

    test = raterro.RAterro('test/sample12x12.ppm', 6)
    test.wdf()

if __name__ == "__main__":
    import os
    parentdir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0,parentdir)

    import sys

    if sys.argv[1] == 'aterro':
        aterro()
    elif sys.argv[1] == 'raterro':
        raterro()
