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

import ppm

# Some conventions:
# 
# red: set J (source of soil)
# green: set A (destination of soil)
def get_dist(f_name, t=0):
    """Get distance between points
    t: type of distance
    """
    # TODO Write function.
    pass

def get_valid_paths(f_name):
    """Get valid paths
    
    The valid path is based on Bresenham line algorithm.
    """
    p_map = ppm.PPM(f_name)
    r = p_map.get_row()
    c = p_map.get_col()
    for j_i in xrange(r):
        for j_j in xrange(c):
            if is_j(p_map.get_color(j_i, j_j)):
                for a_i in xrange(r):
                    for a_j in xrange(c):
                        if (j_i, j_j) != (a_i, a_j) and is_a(p_map.get_color(a_i, a_j)):
                            print("({0}, {1}, {2}, {3})".format(j_i, j_j, a_i, a_j)

def is_j(p_map):
    r = False
    try:
        if 0 < p_map[0] <= 255 and p_map[1] == 0 and p_map[2] == 0:
            r = True
    except:
        pass
    return r

def is_a(p_map):
    r = False
    try:
        if  p_map[0] == 0 and 0 < p_map[1] <= 255 and p_map[2] == 0:
            r = True
    except:
        pass
    return r
