#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

p = re.compile(r'(=+).+\1')
with open('english-article.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        m = p.match(line)
        if m:
            print('レベル：{}'.format(line.count('=') // 2 - 1), '\t', 
                  'セクション名：{}'.format(line.replace('=', '')).strip())