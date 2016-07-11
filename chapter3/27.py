#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

p1 = re.compile(r'(\'{5}|\'{3})(.+?)\1')
p2 = re.compile(r'\[\[(.+?)\]\]')
with open('english-article.txt', 'r') as f:
    for line in f:
        line = p1.sub(r'\2', line.strip('\n'))
        m = p2.search(line)
        if m:
            line = p2.sub(r'\1', line.strip('\n'))
        else:
            line = line.strip('\n')
        print(line)