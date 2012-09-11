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
# blue: set B (barrier)
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
                            for p_i in xrange(r):
                                for p_j in xrange(c):
                                    if (j_i, j_j) != (p_i, p_j) and (a_i, a_j) != (p_i, p_j) and not is_b(p_map.get_color(p_i, p_j)):
                                        if try_path(p_map, (j_i, j_j), (a_i, a_j), (p_i, p_j)):
                                            print("({0}, {1}, {2}, {3}, {4}, {5})".format(j_i, j_j, a_i, a_j, p_i, p_j))

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

def is_b(p_map):
    r = False
    try:
        if p_map[0] == 0 and p_map[1] == 0 and 0 < p_map[2] <= 255:
            r = True
    except:
        pass
    return r

def try_path(p_map, j, a, p):
    """Try Path from j to a passing in p for p_map

    Use the Bresenham line algorithm.
    """
    r = True
    if not try_line(p_map, j, p) or not try_line(p_map, p, a):
        r = False
    return r

def try_line(p_map, s, d):
    """Try line from s to d for p_map
    """
    r = True
    s = list(s)
    d = list(d)
    steep = abs(d[1] - s[1]) > abs(d[0] - s[0])
    if steep:
        s[0], s[1] = s[1], s[0]
        d[0], d[1] = d[1], d[0]
    if s[0] > d[0]:
        s, d = d, s
    deltax = int(d[0] - s[0])
    deltay = int(abs(d[1] - s[1]))
    error = 0.0
    deltaerr = abs(deltay / deltax)
    if s[1] < d[1]:
        ystep = 1
    else:
        ystep = -1
    y = s[1]
    for x in xrange(s[0], d[0] + 1):
        if steep:
            if is_b(p_map.get_color(y, x)):
                r = False
                break
        else:
            if is_b(p_map.get_color(y, x)):
                r = False
                break
        error = error + deltaerr
        if error >= 0.5:
            y = y + ystep
            error = error - 1
    return r
