Criando Imagens para Teste
==========================

Por convensão, a jazida é representada pela cor vermelha, o aterro pela cor
verde e o obstáculo pela cor azul. Essas regiões não devem ser delimitadas por
nenhum contorno e as demais devem ser brancas ou transparente.

Para criar novos mapas, recomenda-se utilizar o Inkscape e salvar o mapa no
formato svg.

Para converter o arquivo svg para o formato ppm (em ASCII, P3), recomenda-se
utilizar o ImageMagick por meio do comando `convert` como indicado abaixo: ::

    $ convert input.svg -compress none -scale <n>x<n> -depth 8 output.ppm

A opção `<n>` corresponde ao número de pixels que o arquivo de saída irá possuir
em cada uma das dimensões. Para gerar uma imagem com 120 pixels por 120 pixels
::

    $ convert input.svg -compress none -scale 120x120 -depth 8 output.ppm

e para uma imagem com 480 por 480 ::

    $ convert input.svg -compress none -scale 480x480 -depth 8 output.ppm

