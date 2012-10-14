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
import aterro

class RAterro(aterro.Aterro):
    """RAterro Aterro with restriction
    This class store information of aterro with restriction.

    Some conventions:

        red: set J (source of soil)

        green: set A (destination of soil)

        blue: set R (restriction)

    Example:

    Create:

        >>> import aterro
        >>> test = raterro.RAterro('test/sample.ppm.', 100, 800)
    """
    def __init__(self, f_name, preduce, D):
        """Constructor

        :param f_name: name of ppm file.

        :type f_name: string.

        :param preduce: number of vertical and horizontal pixels to be reduce to
        one.

        :type preduce: integer.

        :param D: max distance between two points.

        :type D: float.
        """
        aterro.Aterro.__init__(self, f_name, preduce, D)
        self.r = []
        self.h = []

    def _is_r(self, p):
        """Return true if point belong to R.

        :param p: coordinates of point.

        :type p: tuple.

        :return: true if point belong to R.

        :rtype: boolean.
        """
        c = self.map.get_color(p)
        r = False
        try:
            if (c[0] < self.map.max_color / 10 and c[1] < self.map.max_color / 10
                    and  0 < c[2] < self.map.max_color):
                r = True
        except:
            pass
        return r

    def _who_is_r(self):
        """Return a list of tuples of points belong to R.

        :return: points belong to R.

        :rtype: list.
        """
        aux = []
        for i in xrange(self.map.get_row()):
            for j in xrange(self.map.get_col()):
                if self._is_r((i, j)):
                    aux.append((i, j))
        return aux

    def _who_is_h(self):
        """Return a list of tuples of points not belong to J, A nor R.

        :return: points not belong to J, A nor R.

        :rtype: list.
        """
        aux = []
        for i in xrange(self.map.get_row()):
            for j in xrange(self.map.get_col()):
                if (not self._is_j((i, j)) and
                        not self._is_a((i, j)) and
                        not self._is_r((i, j))):
                    aux.append((i, j))
        return aux

    def _try_line(self, o, d):
        """Try line from o to d.

        :param o: point of origin.
        
        :type o: tuple.

        :param d: point of destination.
        
        :type d: tuple.

        :return: true if line is valid.

        :rtype: boolean.

        ALGORITHM:

        Use the Bresenham line algorithm.
        """
        # 'tuple' object does not support item assignment
        o = list(o)
        d = list(d)

        r = True
        if o == d:
            r = False
        else:
            steep = abs(d[1] - o[1]) > abs(d[0] - o[0])
            if steep:
                o[0], o[1] = o[1], o[0]
                d[0], d[1] = d[1], d[0]
            if o[0] > d[0]:
                o, d = d, o
            deltax = int(d[0] - o[0])
            deltay = int(abs(d[1] - o[1]))
            error = 0.0
            deltaerr = abs(deltay / deltax)
            if o[1] < d[1]:
                ystep = 1
            else:
                ystep = -1
            y = o[1]
            for x in xrange(o[0], d[0] + 1):
                if steep:
                    if self._is_r((x, y)):
                        r = False
                        break
                else:
                    if self._is_r((x, y)):
                        r = False
                        break
                error = error + deltaerr
                if error >= 0.5:
                    y = y + ystep
                    error = error - 1
        return r

    def _try_path(self, o, p, d):
        """Try Path from o to d passing in p.

        :param o: coordinates of the point of origin.

        :type o: tuple.

        :param p: coordinates of the point of pivot.

        :type p: tuple.

        :param d: coordinates of the point of destination.

        :type d: tuple.

        :return: true if path is valid.

        :treturn: boolean.
        """
        r = True
        if not self._try_line(o, p) or not self._try_line(p, d):
            r = False
        return r

    def _path_is_valid(self, o, p, d, t=0):
        """Get if path between o and d is valid passing by point p.

        :param o: coordinates of the point of origin.

        :type o: tuple.

        :param p: coordinates of the point of pivot.

        :type p: tuple.

        :param d: coordinates of the point of destination.

        :type d: tuple.

        :param t: type of distance.

        :type t: integer.

        :return: true if path is valid.

        :treturn: boolean.
        """
        valid = False
        if self._try_path(o, p, d):
            if t == 1:
                if (self.map.dl(o, p) < self.D and
                        self.map.dl(p, d) < self.D):
                    valid = True
            elif t == 2:
                if (self.map.du(o, p) < self.D and
                        self.map.du(p, d) < self.D):
                    valid = True
            else:
                if (self.map.dc(o, p) < self.D and
                        self.map.dc(p, d) < self.D):
                    valid = True
        return valid

    def _who_is_valid_path(self):
        """ Return a list of tuples where the last position is a list of the
        possible pivot, for the origin and destinity specify by the other
        position of the tuple.

        :return: valid paths.

        :rtype: tuple of list.
        """
        aux = []
        for (j_i, j_j) in self.j:
            for (a_i, a_j) in self.a:
                l = []
                for (h_i, h_j) in self.h:
                    if self._path_is_valid(
                            (j_i, j_j), (h_i, h_j), (a_i, a_j)):
                        l.append((h_i, h_j))
                aux.append((j_i, j_j, a_i, a_j, l))
        return aux

    def wdf(self, t=0):
        """Write data file.

        :param t: type of distance

        * ``0``: the distance between centers.
        * ``1``: the minimum distance.
        * ``2``: the maximum distance.

        :type t: integer

        .. deprecated:: ef9b47c42656b1cf45ed2d18e5f1c2b1c659e1df
        
            Use :meth:`wpf` instead.
        """
        # Build attributes.
        if not self.info:
            self.j = self._who_is_j()
            self.phi = self._phi()
            self.a = self._who_is_a()
            self.psi = self._psi()
            self.r = self._who_is_r()
            self.h = self._who_is_h()
            self.valid_paths = self._who_is_valid_path()

        sys.stdout = open(self.f_name.replace(
            ".ppm", "_raterro.dat"), 'w+')
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
                if self._is_j((i, j)):
                    print("({0}, {1})".format(i, j))
        print(";")
        print("set A := ");
        for i in xrange(r):
            for j in xrange(c):
                if self._is_a((i, j)):
                    print("({0}, {1})".format(i, j))
        print(";")
        print("set P := ");
        for i in xrange(r):
            for j in xrange(c):
                if (not self._is_j((i, j))
                        and not self._is_a((i, j))
                        and not self._is_r((i, j))):
                    print("({0}, {1})".format(i, j))
        print(";")

        # Definicao dos valores para J e A.
        print("param phi :=")
        begin = True
        for i in xrange(r):
            for j in xrange(c):
                if self._is_j((i, j)):
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
                if self._is_a((i, j)):
                    if begin:
                        begin = False
                        print("[{0}, {1}] {2}".format(
                            i, j, self.map.get_green((i, j))))
                    else:
                        print(", [{0}, {1}] {2}".format(
                            i, j, self.map.get_green((i, j))))
        print(";")

        v = open(self.f_name.replace(
            ".ppm", "_raterro.val"), 'w+')
        print("set too_long :=")
        for j_i in xrange(r):
            for j_j in xrange(c):
                for a_i in xrange(r):
                    for a_j in xrange(c):
                        for p_i in xrange(r):
                            for p_j in xrange(c):
                                if not self.path_is_valid(
                                        (j_i, j_j), (p_i, p_j),
                                        (a_i, a_j), t):
                                    print("({0}, {1}, {2}, {3}, {4}, {5})".format(
                                        j_i, j_j, p_i, p_j, a_i, a_j))
                                else:
                                    v.write("({0}, {1}, {2}, {3}, {4}, {5})\n".format(
                                        j_i, j_j, p_i, p_j, a_i, a_j))


        print(";")
        print("end;")
        sys.stdout.close()
        sys.stdout = sys.__stdout__

    def wpf(self, pf_name = None):
        """Write pickle file.

        :param d_type: type of the distance to be use.

        * ``0``: the distance between centers.
        * ``1``: the minimum distance.
        * ``2``: the maximum distance.

        :type d_type: integer.

        :param pf_name: name to use for the pickle file.  If None, than
            self.f_name is used.

        :type pf_name: string.
        """
        import pickle

        # Build attributes.
        if not self.info:
            self.j = self._who_is_j()
            self.phi = self._phi()
            self.a = self._who_is_a()
            self.psi = self._psi()
            self.r = self._who_is_r()
            self.h = self._who_is_h()
            self.valid_paths = self._who_is_valid_path(d_type)

        if not pf_name:
            pf_name = self.f_name.replace('.ppm',
                    '_raterro{0}-{1}.pickle'.format(self.preduce, d_type))
        print("Try to write data in {0}.".format(pf_name))
        with open(pf_name, 'wb') as f:
            pickle.dump({"m": self.map.get_row(), "n": self.map.get_col(),
                    "j": self.j, "a": self.a,
                    "phi": self.phi, "psi": self.psi,
                    "p": self.valid_paths}, f)
        print("Data sucessfully write in {0}.".format(pf_name))
