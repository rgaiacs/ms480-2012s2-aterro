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

# Dimensao da malha quadriculada
param n, integer, > 0;
param m, integer, > 0;

# Definicao do conjunto referente a malha quadriculada.
set N, dimen 1, := {0..n - 1};
set M, dimen 1, := {0..m - 1};

# Definicao do conjunto J e A.
set J, dimen 2;
set A, dimen 2;
set P, dimen 2;

# Definicao dos valores para J e A.
param phi{J};
param psi{A};

# Definicao do conjunto de pares nao utilizados.
set too_long, dimen 6;

# Definicao das variaveis.
var xi{N, M, N, M, N, M}, >= 0;

# Restricoes.
s.t. lim_d{(x1, x2, z1, z2, y1, y2) in too_long}:
    xi[x1, x2, z1, z2, y1, y2], = 0;
s.t. lim_j{(x1, x2) in J, (z1, z2) in P}:
    sum{(y1, y2) in A} xi[x1, x2, z1, z2, y1, y2], <= phi[x1, x2];
s.t. lim_a{(y1, y2) in A, (z1, z2) in P}:
    sum{(x1, x2) in J} xi[x1, x2, z1, z2, y1, y2], <= psi[y1, y2];

# Funcao objetivo.
maximize obj:
    sum{(x1, x2) in J, (z1, z2) in P, (y1, y2) in A} xi[x1, x2, z1, z2, y1, y2];

end;
