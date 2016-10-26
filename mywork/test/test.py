#!/usr/bin/env python
# coding=utf-8

nRange = [300, 200, 400, 50,5000,10000]

def test(num,nRange):
    nRange.sort()
    print (nRange)
    for n in nRange:
        if num <  n:
            if nRange.index(n) > 0:
                return nRange[nRange.index(n) - 1]
            else:
                return 0
        elif num == n:
            return n
while 1:

    num = float(input("> "))

    print (test(num, nRange))

