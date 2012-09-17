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

import sys
import ppm

class Aterro:
    """Aterro Aterro
    This class store information of aterro.

    Some conventions:

        red: set J (source of soil)
        green: set A (destination of soil)

    Example:

    Create:

        >>> import aterro
        >>> test = aterro.Aterro('test/minimal.ppm', 3)
        >>> test.wdf()
    """
    def __init__(self, f_name, D):
        """Constructor

        :param f_name: name of ppm file.

        :type f_name: string.

        :param D: max distance between points.
        
        :type D: float.
        """
        self.f_name = f_name
        self.map = ppm.PPM(f_name)
        self.D = D

    def is_j(self, p):
        """Return true if point belong to J.

        :param p: coordinates of point.

        :type p: tuple.

        :return: true if point belong to J.

        :rtype: boolean.
        """
        c = self.map.get_color(p)
        r = False
        try:
            if 0 < c[0] <= 255 and c[1] == 0 and c[2] == 0:
                r = True
        except:
            pass
        return r

    def is_a(self, p):
        """Return true if point belong to A.

        :param p: coordinates of point.

        :type p: tuple.

        :return: true if point belong to A.

        :rtype: boolean.
        """
        c = self.map.get_color(p)
        r = False
        try:
            if c[0] == 0 and 0 < c[1] <= 255 and c[2] == 0:
                r = True
        except:
            pass
        return r

    def path_is_valid(self, o, d, t=0):
        """Get if path between o and d is valid.

        :param o: coordinates of the point of origin.

        :type o: tuple.

        :param d: coordinates of the point of destination.

        :type d: tuple.

        :param t: type of distance

        :type t: integer

        :return: true if the path is valid.

        :rtype: boolean.
        """
        valid = False
        if t == 1:
            if self.map.dl(o, d) < self.D:
                valid = True
        elif t == 2:
            if self.map.du(o, d) < self.D:
                valid = True
        else:
            if self.map.dc(o, d) < self.D:
                valid = True
        return valid

    def wdf(self, t=0):
        """Write data file.

        :param t: type of distance

        :type t: integer
        """
        sys.stdout = open(self.f_name.replace(
            ".ppm", "_aterro.dat"), 'w+')
        print("data;")

        # Dimensao da malha.
        r = self.map.get_row()
        c = self.map.get_col()
        print("param n := {0};".format(r))
        print("param m := {0};".format(c))

        # Definicao do conjunto J e A.
        print("set J := ");
        for i in xrange(r):
            for j in xrange(c):
                if self.is_j((i, j)):
                    print("({0}, {1})".format(i, j))
        print(";")
        print("set A := ");
        for i in xrange(r):
            for j in xrange(c):
                if self.is_a((i, j)):
                    print("({0}, {1})".format(i, j))
        print(";")

        # Definicao dos valores para J e A.
        print("param phi :=")
        begin = True
        for i in xrange(r):
            for j in xrange(c):
                if self.is_j((i, j)):
                    if begin:
                        begin = False
                        print("[{0}, {1}] {2}".format(
                            i, j, self.map.get_red((i, j))))
                    else:
                        print(", [{0}, {1}] {2}".format(
                            i, j, self.map.get_red((i, j))))
        print(";")
        print("param psi :=")
        begin = True
        for i in xrange(r):
            for j in xrange(c):
                if self.is_a((i, j)):
                    if begin:
                        begin = False
                        print("[{0}, {1}] {2}".format(
                            i, j, self.map.get_green((i, j))))
                    else:
                        print(", [{0}, {1}] {2}".format(
                            i, j, self.map.get_green((i, j))))
        print(";")

        print("set too_long :=")
        for j_i in xrange(r):
            for j_j in xrange(c):
                for a_i in xrange(r):
                    for a_j in xrange(c):
                        if not self.path_is_valid(
                                (j_i, j_j), (a_i, a_j), t):
                            print("({0}, {1}, {2}, {3})". format(
                                j_i, j_j, a_i, a_j))

        print(";")
        print("end;")
        sys.stdout.close()
        sys.stdout = sys.__stdout__
