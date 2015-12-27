# -*- coding:utf-8 -*-
__author__ = 'Gree-gorey'

from treetagger import TreeTagger
import codecs
import time
import os

t1 = time.time()

tt = TreeTagger(encoding=u'utf-8',language=u'russian')

def read_texts():
    for root, dirs, files in os.walk(u'/home/gree-gorey/Py/Poetry/Corpus'):
        for filename in files:
            if u'txt' in filename:
                open_name = u'/home/gree-gorey/Py/Poetry/Corpus/' + filename
                f = codecs.open(open_name, 'r', 'utf-8')
                text = f.read()
                f.close()
                yield text, open_name

for item in read_texts():
    print item[1]
    ann = tt.tag(item[0])
    writeName = item[1].replace(u'txt', u'ann')
    w = codecs.open(writeName, 'w', 'utf-8')
    try:
        for token in ann:
            w.write(token[0] + u'\t' + token[1] + u'\t' + token[2] + u'\n')
    except:
        pass
    w.close()


t2 = time.time()
print t2 - t1