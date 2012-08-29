# This file is part of 'Experimentos Computacionais de MS480 - 2012S2 - Aterro com Obstaculo'.
#
# Copyright (c) 2012 Raniere Silva <r.gaia.cs@gmail.com>
#
# 'Experimentos Computacionais de MS480 - 2012S2 - Aterro com Obstaculo' is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
#
import sys
import aterro

f = open('test/test.out', 'w')
sys.stdout = f
aterro.get_valid_paths('test/sample_12x12.ppm')
sys.stdout = sys.__stdout__
f.close()
