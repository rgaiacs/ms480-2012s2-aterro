Como Testar
===========

Para testar se existe algum erro de sintaxe no modelo, utilize. ::

    $ cd src
    $ python test/test.py aterro
    $ python test/test.py raterro

Para resolver o modelo, utilise: ::

    $ cd src
    $ python test/test.py aterro solve
    $ python test/test.py raterro solve

É possível informar o arquivo ppm a ser utilizado para teste (se nenhum arquivo
for informado é utilizado o `sample12x12.ppm`). ::

    $ cd src
    $ python test/test.py aterro sample60x60.ppm
    $ python test/test.py aterro solve sample60x60.ppm
    $ python test/test.py raterro sample60x60.ppm
    $ python test/test.py raterro solve sample60x60.ppm
