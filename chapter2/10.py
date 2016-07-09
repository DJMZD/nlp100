#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('hightemp.txt', 'r') as f:
    count = 0
    for line in f:
        count += 1

print('{}行'.format(count))