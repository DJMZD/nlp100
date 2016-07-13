#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter, defaultdict
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt
import pickle

with open('neko.txt.mecab.pickle', 'rb') as f:
    article = pickle.load(f)
    words = [w['base'] for sent in article for w in sent]

word, count = zip(*Counter(words).most_common(10))

w = 0.75
plt.bar(np.arange(10), count, width = w)
plt.xticks(np.arange(10) + w / 2, word)
plt.show()