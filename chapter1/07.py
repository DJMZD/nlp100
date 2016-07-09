#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sFromTemp(x, y, z):
	return '{}時の{}は{}'.format(x, y, z)

if __name__ == '__main__':
	print(sFromTemp(12, '気温', 22.4))