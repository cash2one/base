#!/usr/bin/env python
# coding=utf-8

with open('requirements.txt', 'r') as f1:
    with open('requirements1.txt', 'a+') as f2:
        for line in f1:
            line = line.replace(' (','==')
            line = line.replace(')','')
            
            f2.write(line)
