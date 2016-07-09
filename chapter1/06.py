#!/usr/bin/env python
# -*- coding: utf-8 -*-

def char_ngram(s, n):
	return {s[i: i + n] for i in range(len(s) - n + 1)}

str1 = 'paraparaparadise'
str2 = 'paragraph'

if __name__ == '__main__':
	X = char_ngram(str1, 2)
	Y = char_ngram(str2, 2)

	print('X = ', X)
	print('Y = ', Y)
	print('和集合 = ', (X | Y))
	print('差集合 = ', (X - Y))
	print('積集合 = ', (X & Y))
	if 'se' in X: print('"se" is in X')
	if 'se' in Y: print('"se" is in Y')