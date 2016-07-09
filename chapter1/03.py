#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

s = '''Now I need a drink, alcoholic of course, after the heavy lectures 
		#involving quantum mechanics'''

#p = re.compile('[.,]')
#char_count = [len(p.sub('', word)) for word in s.split()]

char_count = [len(word.strip('.,')) for word in s.split()]
print(char_count)