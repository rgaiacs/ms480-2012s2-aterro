#!/bin/sh
set e-
python test/test.py --pickle --psolve --preduce 100
python test/test.py -b 1 --pickle --psolve --preduce 100
python test/test.py -b 2 550 421 98 --pickle --psolve --preduce 100
python test/test.py --pickle --psolve --preduce 50
python test/test.py -b 1 --pickle --psolve --preduce 50
python test/test.py -b 2 550 421 98 --pickle --psolve --preduce 50
# python test/test.py --pickle --psolve --preduce 25
# python test/test.py -b 1 --pickle --psolve --preduce 25
# python test/test.py -b 2 550 421 98 --pickle --psolve --preduce 25
python test/test.py --pickle --psolve --preduce 100 -f test/t1.ppm
python test/test.py -b 1 --pickle --psolve --preduce 100 -f test/t1.ppm
python test/test.py -b 2 550 421 98 --pickle --psolve --preduce 100 -f test/t1.ppm
python test/test.py --pickle --psolve --preduce 50 -f test/t1.ppm
python test/test.py -b 1 --pickle --psolve --preduce 50 -f test/t1.ppm
python test/test.py -b 2 550 421 98 --pickle --psolve --preduce 50 -f test/t1.ppm
# python test/test.py --pickle --psolve --preduce 25 -f test/t1.ppm
# python test/test.py -b 1 --pickle --psolve --preduce 25 -f test/t1.ppm
# python test/test.py -b 2 550 421 98 --pickle --psolve --preduce 25 -f test/t1.ppm
python test/test.py --pickle --psolve --preduce 100 -f test/t2.ppm
python test/test.py -b 1 --pickle --psolve --preduce 100 -f test/t2.ppm
python test/test.py -b 2 550 421 98 --pickle --psolve --preduce 100 -f test/t2.ppm
python test/test.py --pickle --psolve --preduce 50 -f test/t2.ppm
python test/test.py -b 1 --pickle --psolve --preduce 50 -f test/t2.ppm
python test/test.py -b 2 550 421 98 --pickle --psolve --preduce 50 -f test/t2.ppm
# python test/test.py --pickle --psolve --preduce 25 -f test/t2.ppm
# python test/test.py -b 1 --pickle --psolve --preduce 25 -f test/t2.ppm
# python test/test.py -b 2 550 421 98 --pickle --psolve --preduce 25 -f test/t2.ppm
set e+
