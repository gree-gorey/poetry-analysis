# -*- coding:utf-8 -*-
__author__ = 'Gree-gorey'

import codecs
import time
import os
import scipy.stats

t1 = time.time()

topic = {}

tar = dict([line.rstrip(u'\n').split(u'\t') for line in codecs.open(u'/home/gree-gorey/Py/Poetry/adjectives.txt', u'r', u'utf-8')])
all = dict([line.rstrip(u'\n').split(u'\t') for line in codecs.open(u'/home/gree-gorey/Py/Poetry/adjectivesALL.txt', u'r', u'utf-8')])

with open(u'/home/gree-gorey/Py/Poetry/words.txt') as f:
    words = f.read().decode(u'utf-8').split(u'\n')
    for word in words:
        if word in tar:
            tarFreq = int(tar[word])
        else:
            print word + u'!'
            continue
            tarFreq = 0
        if word in all:
            allFreq = int(all[word])
        else:
            print word
            continue
            allFreq = 0

        arr = [ [ tarFreq, allFreq ], [ (366 - tarFreq), (366 - allFreq) ] ]
        chi2, p, ddof, expected = scipy.stats.chi2_contingency( arr )

        if p <= 0.05:
            topic[word] = (chi2, p)

w = codecs.open(u'/home/gree-gorey/Py/Poetry/topic', u'w', u'utf-8')
for key in topic:
    w.write(key + u'\t' + str(topic[key][0]) + u'\t' + str(topic[key][1]) + u'\n')
w.close()

t2 = time.time()
print t2 - t1
