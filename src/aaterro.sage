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

        sage: minimize_path((-2,0), (2,0), (0,0), 1)
        sage: minimize_path((-2,1), (2,1), (0,0), 1)
        sage: minimize_path((-2,2), (2,2), (0,0), 1)
    """
    # To "simplify" the problem, put the point ``c`` at (0, 0).
    a = (x[0] - c[0], x[1] - c[1])
    b = (y[0] - c[0], y[1] - c[1])

    x = var('x')
    f = lambda p: sqrt((p[0] - a[0])^2 + (p[1] - a[1])^2) + sqrt((p[0] - b[0])^2 + (p[1] - b[1])^2)
    c_1 = lambda p: -r^2 * ((p[0] - a[0])^2 + (p[1] - a[1])^2) + (p[0] * a[1] - p[1] * a[0])^2 - .1
    c_2 = lambda p: -r^2 * ((p[0] - b[0])^2 + (p[1] - b[1])^2) + (p[0] * b[1] - p[1] * b[0])^2 - .1
    sol = minimize_constrained(f, [c_1, c_2], [1,1])

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

        sage: show_mq((-2,0), (2,0), (0,0), 1)
        sage: show_mq((-2,1), (2,1), (0,0), 1)
        sage: show_mq((-2,2), (2,2), (0,0), 1)
    """
    return circle(c, r) + line([x, minimize_path(x, y, c, r), y])

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
        >>> test = raterro.RAterro('test/sample.ppm.', 100, 800)
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

    def _who_is_valid_path(self):
        """ Return a list of tuples where the last position is a list of the
        possible pivot, for the origin and destinity specify by the other
        position of the tuple.

        :return: valid paths.

        :rtype: tuple of list.
        """
        aux = []
        for j in self.j:
            for a in self.a:
                h = minimize_path(j, a, self.c, self.c_r)
                if self._path_is_valid(j, h, a):
                    aux.append(j, a, [h])
        return aux
