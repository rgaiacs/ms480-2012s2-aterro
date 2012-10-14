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

import math

class PPM:
    """PPM Class
    This class store a ppm file.

    Example:

    Load ppm file:
    
        >>> import ppm
        >>> test = ppm.PPM('test/sample.ppm', 100)
    """
    def __init__(self, f_name, preduce):
        """Contructor

        :param f_name: name of ppm file.

        :type f_name: string.

        :param preduce: number of vertical and horizontal pixels to be reduce to
        one.

        :type preduce: integer.
        """
        try:
            f = open(f_name, 'r')
        except:
            raise OSError("Check if {0} exist.".format(f_name))

        # Auxiliar variables.
        col = 0
        row = 0
        max_color = 0
        r = []
        g = []
        b = []

        # Read the figure and store it in the memory.
        l = f.readline()
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        insert2col = 0
        insert2row = 0
        insert2color = 0
        while l != '':
            # Lines begin with # are comments.
            if l[0] != '#':
                ll = l.split()
                for ll_aux in ll:
                    if ll_aux[0] in digits:
                        if col == 0:
                            col = int(ll_aux)
                        elif row == 0:
                            row = int(ll_aux)
                            r = [[0 for i in xrange(col)] for j in xrange(row)]
                            g = [[0 for i in xrange(col)] for j in xrange(row)]
                            b = [[0 for i in xrange(col)] for j in xrange(row)]
                        elif max_color == 0:
                            max_color = int(ll_aux)
                        else:
                            if insert2color == 0:
                                r[insert2row][insert2col] = int(ll_aux)
                                insert2color = (insert2color + 1) % 3
                            elif insert2color == 1:
                                g[insert2row][insert2col] = int(ll_aux)
                                insert2color = (insert2color + 1) % 3
                            elif insert2color == 2:
                                b[insert2row][insert2col] = int(ll_aux)
                                insert2color = (insert2color + 1) % 3
                                insert2col = (insert2col + 1) % col
                                if insert2col == 0:
                                    insert2row = insert2row + 1
            l = f.readline()
        f.close()

        # Reshape the figure.
        self.col = col / preduce
        self.row = row / preduce
        self.max_color = max_color * preduce * preduce
        self.r = [[0 for i in xrange(self.col)] for j in xrange(self.row)]
        self.g = [[0 for i in xrange(self.col)] for j in xrange(self.row)]
        self.b = [[0 for i in xrange(self.col)] for j in xrange(self.row)]
        for i in xrange(self.row):
            for j in xrange(self.col):
                for ir in xrange(preduce):
                    for jr in xrange(preduce):
                        self.r[i][j] += r[i * preduce + ir][j * preduce + jr]
                        self.g[i][j] += g[i * preduce + ir][j * preduce + jr]
                        self.b[i][j] += b[i * preduce + ir][j * preduce + jr]

    def get_row(self):
        """Get number of rows.

        :return: number or rows.

        :rtype: integer.
        """
        return self.row

    def get_col(self):
        """Get number of columns.

        :return: number of columns.

        :rtype: integer.
        """
        return self.col

    def get_color(self, p):
        """Get Color

        :param p: coordinates of point.

        :type p: tuple.

        :return: color of point.

        :rtype: tuple.

        EXAMPLE:

        Get color at (0,0):
        
            >>> test.get_color((0,0))
        """
        return (self.r[p[0]][p[1]], self.g[p[0]][p[1]],
                self.b[p[0]][p[1]])

    def get_red(self, p):
        """Get Red Value

        :param p: coordinates of point.

        :type p: tuple.

        :return: value of red color.

        :rtype: integer.

        EXAMPLE:

        Get red value at (0,0):
        
            >>> test.get_red((0,0))
        """
        return (self.r[p[0]][p[1]])

    def get_green(self, p):
        """Get Green Value

        :param p: coordinates of point.

        :type p: tuple.

        :return: value of green color.

        :rtype: integer.

        EXAMPLE:

        Get red value at (0,0):
        
            >>> test.get_green((0,0))
        """
        return (self.g[p[0]][p[1]])

    def get_blue(self, p):
        """Get Blue Value

        :param p: coordinates of point.

        :type p: tuple.

        :return: value of blue color.

        :rtype: integer.

        EXAMPLE:

        Get red value at (0,0):
        
            >>> test.get_blue((0,0))
        """
        return (self.b[p[0]][p[1]])

    def dl(self, o, d):
        """Compute min distance between o and d.

        :param o: coordinates of origin point.

        :type o: tuple.

        :param d: coordinates of destination point.

        :type d: tuple.

        :return: distance dl.

        :rtype: float.
        """
        dist = float('Infinity')
        # Same point.
        if o[0] == d[0] and o[1] == d[1]:
            dist = 0
        else:
            # Horizontal align.
            if o[0] == d[0]:
                dist = abs(o[1] - d[1]) - 1
            # Vertical align.
            elif o[1] == d[1]:
                dist = abs(o[0] - d[0]) - 1
            else:
                dist = math.sqrt((abs(o[0] - d[0]) - 1)**2 +
                        (abs(o[1] - d[1]) - 1)**2)
        return dist

    def du(self, o, d):
        """Compute max distance between o and a.

        :param o: coordinates of origin point.

        :type o: tuple.

        :param d: coordinates of destination point.

        :type d: tuple.

        :return: distance du.

        :rtype: float.
        """
        dist = float('Infinity')
        # Same point.
        if o[0] == d[0] and o[1] == d[1]:
            dist = 0
        else:
            # Horizontal align.
            if o[0] == d[0]:
                dist = abs(o[1] - d[1]) + 1
            # Vertical align.
            elif o[1] == d[1]:
                dist = abs(o[0] - d[0]) + 1
            else:
                dist = math.sqrt((abs(o[0] - d[0]) + 1)**2 +
                        (abs(o[1] - d[1]) + 1)**2)
        return dist

    def dc(self, o, d):
        """Compute distance between the centers of o and d.

        :param o: coordinates of origin point.

        :type o: tuple.

        :param d: coordinates of destination point.

        :type d: tuple.

        :return: distance dc.

        :rtype: float.
        """
        return math.sqrt((o[0] - d[0])**2 + (o[1] - d[1])**2)
