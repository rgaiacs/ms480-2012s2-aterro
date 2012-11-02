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

import raterro
import math
from scipy.optimize import fmin_cobyla

def minimize_path(x, y, c, r):
    """Solve the problem of minimize the distance between ``x`` and ``y`` not
    passing in the circle with center ``c`` and radius ``r``.

    :param x: the origin point.

    :type x: tuple.

    :param y: the destination point.

    :type y: tuple.

    :param c: the center of the circle.

    :type c: tuple.

    :param r: the radius of the circle.

    :type r: float.

    :return: the point that solve the problem.

    :rtype: tuple.

    Example:

        >>> minimize_path((-2,0), (2,0), (0,0), 1)
        >>> minimize_path((-2,1), (2,1), (0,0), 1)
        >>> minimize_path((-2,2), (2,2), (0,0), 1)
    """
    # To "simplify" the problem, put the point ``c`` at (0, 0).
    a = (x[0] - c[0], x[1] - c[1])
    b = (y[0] - c[0], y[1] - c[1])

    f = lambda p: math.sqrt((p[0] - a[0])**2 + (p[1] - a[1])**2) + math.sqrt((p[0] - b[0])**2 + (p[1] - b[1])**2)
    c_1 = lambda p: -r**2 * ((p[0] - a[0])**2 + (p[1] - a[1])**2) + (p[0] * a[1] - p[1] * a[0])**2 - .1
    c_2 = lambda p: -r**2 * ((p[0] - b[0])**2 + (p[1] - b[1])**2) + (p[0] * b[1] - p[1] * b[0])**2 - .1
    sol = fmin_cobyla(f, [1,1], (c_1, c_2), disp=0)

    # Return the point to it's origina position.
    sol = (sol[0] + c[0], sol[1] + c[1])
    return sol

def show_mq(x, y, c, r):
    """Create a picture representation of the problem and the solution.

    :param x: the origin point.

    :type x: tuple.

    :param y: the destination point.

    :type y: tuple.

    :param c: the center of the circle.

    :type c: tuple.

    :param r: the radius of the circle.

    :type r: float.

    :return: the point that solve the problem.

    :rtype: tuple.

    Example:

        >>> show_mq((-2,0), (2,0), (0,0), 1)
        >>> show_mq((-2,1), (2,1), (0,0), 1)
        >>> show_mq((-2,2), (2,2), (0,0), 1)
    """
    # TODO Replace the folowing line with matplotlib.
    # return circle(c, r) + line([x, minimize_path(x, y, c, r), y])
    raise NotImplementedError('need rewrite the code with matplotlib')

class AAterro(raterro.RAterro):
    """AAterro Aterro with (analytic) restriction
    This class store information of aterro with restriction.

    Some conventions:

        red: set J (source of soil)

        green: set A (destination of soil)

        blue: set R (restriction)

    Example:

    Create:

        >>> import aterro
        >>> test = raterro.RAterro('test/sample.ppm.', (550, 421), 98, 100, 800)
    """
    def __init__(self, f_name, c, r, preduce, D):
        """Constructor

        :param f_name: name of ppm file.

        :type f_name: string.

        :param preduce: number of vertical and horizontal pixels to be reduce to
        one.

        :type preduce: integer.

        :param D: max distance between two points.

        :type D: float.
        """
        raterro.RAterro.__init__(self, f_name, preduce, D)
        self.c = c
        self.c_r = r

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
        if t == 1:
            o2p = self.map.dl(o, p)
            p2d = self.map.dl(p, d)
            if (o2p < self.D and p2d < self.D):
                valid = True
        elif t == 2:
            o2p = self.map.du(o, p)
            p2d = self.map.du(p, d)
            if (o2p < self.D and p2d < self.D):
                valid = True
        else:
            o2p = self.map.dc(o, p)
            p2d = self.map.dc(p, d)
            if (o2p < self.D and p2d < self.D):
                valid = True
        return (valid, o2p + p2d)

    def _who_is_valid_path(self, t=0):
        """ Return a list of tuples where the last position is a list of the
        possible pivot, for the origin and destinity specify by the other
        position of the tuple.

        :return: valid paths.

        :rtype: tuple of list.
        """
        aux = []
        for j_i, j_j in self.j:
            for a_i, a_j in self.a:
                h_i, h_j = minimize_path((j_i, j_j), (a_i, a_j), self.c, self.c_r)
                h_i = int(h_i)
                h_j = int(h_j)
                try_path = self._path_is_valid((j_i, j_j), (h_i, h_j), (a_i, a_j), t)
                if try_path[0]:
                    aux.append((j_i, j_j, h_i, h_j, a_i, a_j, try_path[1]))
        return aux

    def wpf(self, d_type=0, pf_name=None):
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
                    '_aaterro{0}-{1}.pickle'.format(self.preduce, d_type))
        print("Try to write data in {0}.".format(pf_name))
        with open(pf_name, 'wb') as f:
            pickle.dump({"m": self.map.get_row(), "n": self.map.get_col(),
                    "j": self.j, "a": self.a,
                    "phi": self.phi, "psi": self.psi,
                    "p": self.valid_paths}, f)
        print("Data sucessfully write in {0}.".format(pf_name))
