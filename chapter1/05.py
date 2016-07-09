#!/usr/bin/env python
# -*- coding: utf-8 -*-

def char_ngram(s, n):
	return {s[i: i + n] for i in range(len(s) - n + 1)}

def word_ngram(s, n):
	words = [word.strip(',.!?"') for word in s.split()]
	return {' '.join(words[i: i + n]) for i in range(len(words) - n + 1)}

s = 'I am an NLPer'

if __name__ == '__main__':
	print(char_ngram(s, 2))
	print(word_ngram(s, 2))