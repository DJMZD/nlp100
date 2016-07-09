#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = '''Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might 
		Also Sign Peace Security Clause. Arthur King Can'''

words = [word.strip('.') for word in s.split()]
w_map = {}

#w_map = {w[:2 - (i in {1, 5, 6, 7, 8, 9, 15, 16, 19})]:i
            #for i, w in enumerate(s.split(), 1)}

for index, word in enumerate(words, 1):
	l = 1 if index in {1, 5, 6, 7, 8, 9, 15, 16, 19} else 2
	w_map[word[:l]] = index
	#w_map.update({word[:l]:index})

print(w_map)