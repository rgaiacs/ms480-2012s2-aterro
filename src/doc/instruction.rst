Instruções
==========

Esse projeto foi desenvolvido utilizando apenas software livre:

*   Python 2.7.3 (deve ser possível utilizar a versão 3.X);
*   GLPK 4.45 (deve ser possível utilizar a versão 4.47);
*   Python-GLPK, `http://www.dcc.fc.up.pt/~jpp/code/python-glpk/
    <http://www.dcc.fc.up.pt/~jpp/code/python-glpk/>`_;
*   Swig, necessário para o Python-GLPK,
*   Sage, `http://sagemath.org/ <http://sagemath.org/>`_;
*   Inkscape, para construção dos mapas,
*   ImageMagick, para conversão dos mapas para o formato ppm,
*   LaTeX, para o relatório,
*   Sphinx, para a documentação.

Para instalar os softwares utilizados em um GNU/Linux que utilize o sistemas de
pacotes `.deb`, e.g., Debian, Ubuntu, Mint, pode-se utilizar: ::

    # apt-get install python python-glpk
    # apt-add-repository -y ppa:aims/sagemath
    # apt-get update
    # apt-get install sagemath-upstream-binary

Para manipular (criar) novos testes: ::

    # apt-get install inkscape

Para gerar o relatório: ::

    # apt-get install latex

E para a documentação: ::

    # apt-get install sphinx

Para instalar os softwares utilizados em um GNU/Linux que utilize o sistema de
pacotes `.rpm`, basta procurar pelos pacotes de mesmo nome.

Para instalar os softwares utilizados em um GNU/Linux que não utilize os
sistemas de pacotes `.deb` nem `.rpm`, procure os pacotes no gerenciador de
pacotes que utilizar ou baixe e compile os softwares.

Para instalar os softwares utilizados no Windows ou Mac OS X, dê uma olhada em
como instalar cada um dos softwares na página do mesmo.
