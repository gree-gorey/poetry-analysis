# -*- coding:utf-8 -*-
__author__ = 'Gree-gorey'

import codecs
import time
import os

t1 = time.time()

nouns = {}
verbs = {}
adjectives = {}


def read_texts():
    for root, dirs, files in os.walk(u'/home/gree-gorey/Py/Poetry/Corpus'):
        for filename in files:
            if u'ann' in filename:
                open_name = u'/home/gree-gorey/Py/Poetry/Corpus/' + filename
                f = codecs.open(open_name, 'r', 'utf-8')
                text = f.read()
                f.close()
                yield text

for item in read_texts():
    item = item.split(u'\n')
    for line in item:
        line = line.rstrip()
        token = line.split(u'\t')
        try:
            if token[1][0] == u'N':
                if token[2] not in nouns:
                    nouns[token[2]] = 1
                else:
                    nouns[token[2]] += 1
            if token[1][0] == u'V':
                if token[2] not in verbs:
                    verbs[token[2]] = 1
                else:
                    verbs[token[2]] += 1
            if token[1][0] == u'A':
                if token[2] not in adjectives:
                    adjectives[token[2]] = 1
                else:
                    adjectives[token[2]] += 1
        except:
            pass

w = codecs.open(u'/home/gree-gorey/Py/Poetry/nounsALL.txt', 'w', 'utf-8')
for key in sorted(nouns, key=nouns.get, reverse=True):
    w.write(key + u'\t' + str(nouns[key]) + u'\n')
w.close()

w = codecs.open(u'/home/gree-gorey/Py/Poetry/verbsALL.txt', 'w', 'utf-8')
for key in sorted(verbs, key=verbs.get, reverse=True):
    w.write(key + u'\t' + str(verbs[key]) + u'\n')
w.close()

w = codecs.open(u'/home/gree-gorey/Py/Poetry/adjectivesALL.txt', 'w', 'utf-8')
for key in sorted(adjectives, key=adjectives.get, reverse=True):
    w.write(key + u'\t' + str(adjectives[key]) + u'\n')
w.close()

t2 = time.time()
print t2 - t1