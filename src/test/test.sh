#!/bin/sh
python test/test.py --pickle --psolve --preduce 100
python test/test.py -b 1 -pickle --psolve --preduce 100
python test/test.py -b 2 -pickle --psolve --preduce 100
python test/test.py --pickle --psolve --preduce 10
python test/test.py -b 1 -pickle --psolve --preduce 10
python test/test.py -b 2 -pickle --psolve --preduce 10
