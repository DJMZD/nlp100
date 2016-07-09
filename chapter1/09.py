#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import shuffle

def typo(word):
	l = shuffle(list(word[1: -1]))
	return word[0] + ''.join(l) + word[-1]

s = '''I couldn't believe that I could actually understand what I was 
		reading : the phenomenal power of the human mind .'''

if __name__ == '__main__':
	print(' '.join(typo(word) if len(word) > 4
                                else word for word in s.split()))