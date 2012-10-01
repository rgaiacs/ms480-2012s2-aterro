Como Testar
===========

Para gerar os arquivo de dados para teste a partir do(s) arquivo(s) ppm, utilize:
::

    $ cd src
    $ # Para o modelo sem obstaculo.
    $ python test/test.py --pickle
    $ # Para o modelo com obstaculo.
    $ python test/test.py -b --pickle

..  note::
    É possível gerar os dados no formato GMPL. Essa opção é desaconselhada pois
    o problema com barreiras consome muita memória. ::

        $ cd src
        $ # Para o modelo sem obstaculo.
        $ python test/test.py --data
        $ # Para o modelo com obstaculo.
        $ python test/test.py -b --data

Para construir o modelo e resolve-lo, utilize: ::

    $ cd src
    $ # Para o modelo sem obstaculo.
    $ python test/test.py --psolve
    $ # Para o modelo com obstaculo.
    $ python test/test.py -b --psolve

..  note::
    Se estiver utilizando o GMPL, para resolver o modelo utilize: ::

        $ cd src
        $ # Para o modelo sem obstaculo.
        $ python test/test.py --solve
        $ # Para o modelo com obstaculo.
        $ python test/test.py -b --solve

Caso tenha suspeita de algum problema, é possível gerar um arquivo com o modelo
no formato LP utilizando: ::

    $ cd src
    $ # Para o modelo sem obstaculo.
    $ python test/test.py --psolve --debug
    $ # Para o modelo com obstaculo.
    $ python test/test.py -b --psolve --debug

..  note::
    Neste caso o problema não será resolvido.


..  note::
    Se estiver utilizando o GMPL, é possível verificar o modelo por erros de
    sintaxe. Para isso, utilize: ::

        $ cd src
        $ # Para o modelo sem obstaculo.
        $ python test/test.py --check
        $ # ou
        $ python test/test.py --debug
        $ # Para o modelo com obstaculo.
        $ python test/test.py -b --check
        $ # ou
        $ python test/test.py -b --debug

É possível informar o(s) arquivo(s) ppm a ser(em) utilizado para teste (se
nenhum arquivo for informado é utilizado o `sample12x12.ppm`). ::

    $ cd src
    $ # Para o modelo sem obstaculo.
    $ python test/test.py --pickle --psolve -f sample60x60.ppm sample120x120.ppm
    $ # Para o modelo com obstaculo.
    $ python test/test.py -b --pickle --psolve -f sample60x60.ppm sample120x120.ppm
