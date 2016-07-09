#!/usr/bin/env python
# -*- coding: utf-8 -*-

str1 = 'パトカー'
str2 = 'タクシー'

#l = []
#for i in range(len(str1)):
#	l.extend((str1[i], str2[i]))

s = ''.join([c1 + c2 for c1, c2 in zip(str1, str2)])

print(s)