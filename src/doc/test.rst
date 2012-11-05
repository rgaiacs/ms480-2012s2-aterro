Como Testar
===========

Existe uma função a ser utilizada para os testes que é acessível por meio da
linha de comando. A seguir apresentamos como utilizá-la.

Sem Obstáculo
-------------
Para gerar os arquivo de dados para teste a partir do(s) arquivo(s) ppm, utilize:
::

    $ cd src
    $ python test/test.py --pickle

..  note::
    É possível gerar os dados no formato GMPL. Essa opção é desaconselhada (e
    desatualizada) pois o problema com barreiras consome muita memória. ::

        $ cd src
        $ python test/test.py --data

Para construir o modelo e resolve-lo, utilize: ::

    $ cd src
    $ python test/test.py --psolve

..  note::
    Se estiver utilizando o GMPL, para resolver o modelo utilize: ::

        $ cd src
        $ python test/test.py --solve

Caso tenha suspeita de algum problema, é possível gerar um arquivo com o modelo
no formato LP utilizando: ::

    $ cd src
    $ python test/test.py --psolve --debug

..  note::
    Neste caso o problema não será resolvido.

..  note::
    Se estiver utilizando o GMPL, é possível verificar o modelo por erros de
    sintaxe. Para isso, utilize: ::

        $ cd src
        $ python test/test.py --check
        $ # ou
        $ python test/test.py --debug

É possível informar o(s) arquivo(s) ppm a ser(em) utilizado para teste (se
nenhum arquivo for informado é utilizado o `sample.ppm`). ::

    $ cd src
    $ python test/test.py --pickle --psolve -f sample.ppm foo.ppm bar.ppm

Obstáculo Circular
------------------
Para gerar os arquivo de dados para teste a partir do(s) arquivo(s) ppm, utilize:
::

    $ cd src
    $ python test/test.py -b 2 c1 c2 r --pickle

onde ``(c1, c2)`` é o centro do círculo e ``r`` é o raio.

Para construir o modelo e resolve-lo, utilize: ::

    $ cd src
    $ python test/test.py -b 2 c1 c2 r --psolve

Caso tenha suspeita de algum problema, é possível gerar um arquivo com o modelo
no formato LP utilizando: ::

    $ cd src
    $ python test/test.py -b 2 c1 c2 r --psolve --debug

..  note::
    Neste caso o problema não será resolvido.

É possível informar o(s) arquivo(s) ppm a ser(em) utilizado para teste (se
nenhum arquivo for informado é utilizado o `sample.ppm`). ::

    $ cd src
    $ python test/test.py -b 2 c1 c2 r --pickle --psolve -f sample.ppm foo.ppm bar.ppm

Obstáculo Genérico
------------------

Para gerar os arquivo de dados para teste a partir do(s) arquivo(s) ppm, utilize:
::

    $ cd src
    $ python test/test.py -b 1 --pickle

..  note::
    É possível gerar os dados no formato GMPL. Essa opção é desaconselhada (e
    desatualizada) pois o problema com barreiras consome muita memória. ::

        $ cd src
        $ python test/test.py -b 1 --data

Para construir o modelo e resolve-lo, utilize: ::

    $ cd src
    $ python test/test.py -b 1 --psolve

..  note::
    Se estiver utilizando o GMPL, para resolver o modelo utilize: ::

        $ cd src
        $ python test/test.py -b 1 --solve

Caso tenha suspeita de algum problema, é possível gerar um arquivo com o modelo
no formato LP utilizando: ::

    $ cd src
    $ python test/test.py -b 1 --psolve --debug

..  note::
    Neste caso o problema não será resolvido.

..  note::
    Se estiver utilizando o GMPL, é possível verificar o modelo por erros de
    sintaxe. Para isso, utilize: ::

        $ cd src
        $ python test/test.py -b 1 --check
        $ # ou
        $ python test/test.py -b 1 --debug

É possível informar o(s) arquivo(s) ppm a ser(em) utilizado para teste (se
nenhum arquivo for informado é utilizado o `sample.ppm`). ::

    $ cd src
    $ python test/test.py -b 1 --pickle --psolve -f sample.ppm foo.ppm bar.ppm
