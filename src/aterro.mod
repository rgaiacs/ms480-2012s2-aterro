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
set N, dimen 1, := {1..n};
set M, dimen 1, := {1..m};

# Definicao do conjunto J e A.
set J, dimen 2;
set A, dimen 2;

# Definicao dos valores para J e A.
param phi{J};
param psi{A};

# Definicao do conjunto de pares nao utilizados.
set too_long, dimen 2;

# Definicao das variaveis.
var xi{N, M, N, M}, >= 0;

# Restricoes.
s.t. lim_d{l in too_long}:
    xi[l[1], l[2]], = 0;
s.t. lim_j{x in J}:
    sum{y in A} xi[x[1], x[2], y[1], y[2]], <= phi[x[1], x[2]];
s.t. lim_a{y in A}:
    sum{x in J} xi[x[1], x[2], y[1], y[2]], <= psi[x[1], x[2]];

# Funcao objetivo.
maximize obj:
    sum{x in J, y in A} xi[x[1], x[2], y[1], y[2]];
