#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('hightemp.txt', 'r') as f:
    f1 = open('col1.txt', 'w')
    f2 = open('col2.txt', 'w')
    for line in f:
        f1.write('{}\n'.format(line.split()[0]))
        f2.write('{}\n'.format(line.split()[1]))
    f1.close()
    f2.close()