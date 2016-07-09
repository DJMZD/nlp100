#!/usr/bin/env python
# -*- coding: utf-8 -*-

f1 = open('col1.txt', 'r')
f2 = open('col2.txt', 'r')
s = '\n'.join([s1.strip('\n') + ' ' + s2.strip('\n') for s1, s2 in zip(f1, f2)])
f1.close()
f2.close()
with open('col1-2.txt', 'w') as f:
    f.write(s)