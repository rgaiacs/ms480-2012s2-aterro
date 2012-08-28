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
class PPM:
    """PPM Class
    This class store a ppm file.

    Example:

    Load ppm file:
    
        >>> import ppm
        >>> test = ppm.PPM('test/minimal.ppm')
    """
    def __init__(self, f_name):
        try:
            f = open(f_name, 'r')
        except:
            print("Check if {0} exist.".format(f_name))
        l = f.readline()
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.col = 0
        self.row = 0
        self.max_color = 0
        self.r = []
        self.g = []
        self.b = []
        insert2col = 0
        insert2row = 0
        insert2color = 0
        while l != '':
            if l[0] != '#':
                ll = l.split()
                for ll_aux in ll:
                    if ll_aux[0] in digits:
                        if self.col == 0:
                            self.col = int(ll_aux)
                        elif self.row == 0:
                            self.row = int(ll_aux)
                            self.r = [[0 for i in xrange(self.col)] for j in xrange(self.row)]
                            self.g = [[0 for i in xrange(self.col)] for j in xrange(self.row)]
                            self.b = [[0 for i in xrange(self.col)] for j in xrange(self.row)]
                        elif self.max_color == 0:
                            self.max_color = int(ll_aux)
                        else:
                            if insert2color == 0:
                                self.r[insert2row][insert2col] = int(ll_aux)
                                insert2color = (insert2color + 1) % 3
                            elif insert2color == 1:
                                self.g[insert2row][insert2col] = int(ll_aux)
                                insert2color = (insert2color + 1) % 3
                            elif insert2color == 2:
                                self.b[insert2row][insert2col] = int(ll_aux)
                                insert2color = (insert2color + 1) % 3
                                insert2col = (insert2col + 1) % self.col
                                if insert2col == 0:
                                    insert2row = insert2row + 1
            l = f.readline()
        f.close()

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_color(self, i, j):
        """Get Color
        i: row number
        j: column number

        Example:

        Get color at (0,0):
        
            >>> test.get_color(0,0)
        """
        return (self.r[i][j], self.g[i][j], self.b[i][j])
