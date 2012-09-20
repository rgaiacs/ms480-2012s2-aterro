Como Testar
===========

Para gerar os arquivo de dados para teste a partir do(s) arquivo(s) ppm, utilize:
::

    $ cd src
    $ # Para o modelo sem obstaculo.
    $ python test/test.py --data
    $ # Para o modelo com obstaculo.
    $ python test/test.py -b --data

Para verificar se existe algum erro de sintaxe no modelo e dados, utilize. ::

    $ cd src
    $ # Para o modelo sem obstaculo.
    $ python test/test.py --check
    $ # Para o modelo com obstaculo.
    $ python test/test.py -b --check

Para resolver o modelo, utilise: ::

    $ cd src
    $ # Para o modelo sem obstaculo.
    $ python test/test.py --solve
    $ # Para o modelo com obstaculo.
    $ python test/test.py -b --solve

É possível informar o(s) arquivo(s) ppm a ser(em) utilizado para teste (se
nenhum arquivo for informado é utilizado o `sample12x12.ppm`). ::

    $ cd src
    $ # Para o modelo sem obstaculo.
    $ python test/test.py --data --solve -f sample60x60.ppm sample120x120.ppm
    $ # Para o modelo com obstaculo.
    $ python test/test.py -b --data --solve -f sample60x60.ppm sample120x120.ppm
