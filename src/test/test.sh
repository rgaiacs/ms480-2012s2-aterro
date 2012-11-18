#!/bin/sh
for preduce in 100 50
do
    for dtype in 0 1 2
    do
        for maxd in 800 900 1000
        do
            python test/test.py --pickle --psolve --preduce $preduce --maxd $maxd --dtype $dtype
            python test/test.py -b 1 --pickle --psolve --preduce $preduce --maxd $maxd --dtype $dtype
            python test/test.py -b 2 550 421 98 --pickle --psolve --preduce $preduce --maxd $maxd --dtype $dtype
            for f in 'test/t1.ppm' 'test/t2.ppm'
            do
                python test/test.py --pickle --psolve --preduce $preduce --maxd $maxd --dtype $dtype -f $f
                python test/test.py -b 1 --pickle --psolve --preduce $preduce --maxd $maxd --dtype $dtype -f $f
                python test/test.py -b 2 550 421 98 --pickle --psolve --preduce $preduce --maxd $maxd --dtype $dtype -f $f
            done
        done
    done
done
