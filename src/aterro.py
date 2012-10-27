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

        >>> import aterro
        >>> test = aterro.Aterro('test/sample.ppm', 100, 800)
    """
    def __init__(self, f_name, preduce, D):
        """Constructor

        :param f_name: name of ppm file.

        :type f_name: string.

        :param preduce: number of vertical and horizontal pixels to be reduce to
        one.

        :type preduce: integer.

        :param D: max distance between points.
        
        :type D: float.
        """
        self.f_name = f_name
        self.preduce = preduce
        self.map = ppm.PPM(f_name, preduce)
        self.D = D / preduce
        self.info = False
        self.j = []
        self.phi = []
        self.a = []
        self.psi = []
        self.valid_paths = []

    def _is_j(self, p):
        """Return true if point belong to J.

        :param p: coordinates of point.

        :type p: tuple.

        :return: true if point belong to J.

        :rtype: boolean.
        """
        c = self.map.get_color(p)
        r = False
        try:
            # There is a 10% of error in the mesuare of the colors.
            if (0 < c[0] <= self.map.max_color and c[1] < self.map.max_color / 10
                    and c[2] < self.map.max_color / 10):
                r = True
        except:
            pass
        return r

    def _who_is_j(self):
        """Return a list of tuples of points belong to J.

        :return: poins belong to J.

        :rtype: list.
        """
        aux = []
        for i in xrange(self.map.get_row()):
            for j in xrange(self.map.get_col()):
                if self._is_j((i, j)):
                    aux.append((i, j))
        return aux

    def _phi(self):
        """Set vector of phi values.

        :return: phi values.

        :rtype: list.
        """
        aux = []
        for p in self.j:
            aux.append(self.map.get_red(p))
        return aux

    def _is_a(self, p):
        """Return true if point belong to A.

        :param p: coordinates of point.

        :type p: tuple.

        :return: true if point belong to A.

        :rtype: boolean.
        """
        c = self.map.get_color(p)
        r = False
        try:
            # There is a 10% of error in the mesuare of the colors.
            if (c[0] < self.map.max_color / 10 and 0 < c[1] <= self.map.max_color
                    and c[2] < self.map.max_color / 10):
                r = True
        except:
            pass
        return r

    def _who_is_a(self):
        """Return a list of tuples of points belong to A.

        :return: poins belong to A.

        :rtype: list.
        """
        aux = []
        for i in xrange(self.map.get_row()):
            for j in xrange(self.map.get_col()):
                if self._is_a((i, j)):
                    aux.append((i, j))
        return aux

    def _psi(self):
        """Set vector of psi values.

        :return: psi values.

        :rtype: list.
        """
        aux = []
        for p in self.a:
            aux.append(self.map.get_green(p))
        return aux

    def _path_is_valid(self, o, d, t=0):
        """Get if path between o and d is valid.

        :param o: coordinates of the point of origin.

        :type o: tuple.

        :param d: coordinates of the point of destination.

        :type d: tuple.

        :param t: type of distance.

        * ``0``: the distance between centers.
        * ``1``: the minimum distance.
        * ``2``: the maximum distance.

        :type t: integer

        :return: true if the path is valid.

        :rtype: boolean.
        """
        valid = False
        if t == 1:
            dist = self.map.dl(o, d)
            if dist < self.D:
                valid = True
        elif t == 2:
            dist = self.map.du(o, d)
            if dist < self.D:
                valid = True
        else:
            dist = self.map.dc(o, d)
            if dist < self.D:
                valid = True
        return valid, dist

    def _who_is_valid_path(self, t):
        """ Return a list of all valid paths.

        :param t: type of distance.

        * ``0``: the distance between centers.
        * ``1``: the minimum distance.
        * ``2``: the maximum distance.

        :type t: integer

        :return: valid paths.

        :rtype: list.
        """
        aux = []
        for j_i, j_j in self.j:
            for a_i, a_j in self.a:
                try_path = self._path_is_valid(
                        (j_i, j_j), (a_i, a_j), t)
                if try_path[0]:
                    aux.append((j_i, j_j, a_i, a_j, try_path[1]))
        return aux

    def wdf(self, t=0):
        """Write data into GMPL file.

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
            self.valid_paths = self._who_is_valid_path()

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
                        if not self._path_is_valid(
                                (j_i, j_j), (a_i, a_j), t):
                            print("({0}, {1}, {2}, {3})". format(
                                j_i, j_j, a_i, a_j))

        print(";")
        print("end;")
        sys.stdout.close()
        sys.stdout = sys.__stdout__

    def wpf(self, d_type=0, pf_name=None):
        """Write pickle file.

        :param d_type: type of the distance to be use.

        * ``0``: the distance between centers.
        * ``1``: the minimum distance.
        * ``2``: the maximum distance.

        :type d_type: integer.

        :param pf_name: name to use for the pickle file. If None, than
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
            self.valid_paths = self._who_is_valid_path(d_type)

        if not pf_name:
            pf_name = self.f_name.replace('.ppm',
                    '_aterro{0}-{1}.pickle'.format(self.preduce, d_type))
        print("Try to write data in {0}.".format(pf_name))
        with open(pf_name, 'wb') as f:
            pickle.dump({"m": self.map.get_row(), "n": self.map.get_col(),
                    "j": self.j, "a": self.a,
                    "phi": self.phi, "psi": self.psi,
                    "p": self.valid_paths}, f)
        print("Data sucessfully write in {0}.".format(pf_name))
