#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cipher(s):
	return ''.join(chr(219 - ord(c)) if 'a' <= c <= 'z' else c for c in s)

s = 'Hello, World!'

if __name__ == '__main__':
	cipher_str = cipher(s)
	print(s)
	print(cipher(s))
	print(cipher(cipher(s)))