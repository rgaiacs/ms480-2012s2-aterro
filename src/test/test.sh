#!/bin/sh
python test/test.py --pickle --psolve --preduce 100
python test/test.py -b 1 --pickle --psolve --preduce 100
python test/test.py -b 2 550 421 98 --pickle --psolve --preduce 100
python test/test.py --pickle --psolve --preduce 10
python test/test.py -b 1 --pickle --psolve --preduce 10
python test/test.py -b 2 550 421 98 --pickle --psolve --preduce 10
