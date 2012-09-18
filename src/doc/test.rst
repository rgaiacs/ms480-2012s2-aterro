Como Testar
===========

Para testar utilize. ::

    $ cd src
    $ python test/test.py aterro
    $ glpsol -m aterro.mod -d test/test/sample12x12_aterro.dat --check
    $ python test/test.py raterro
    $ glpsol -m raterro.mod -d test/test/sample12x12_raterro.dat --check
