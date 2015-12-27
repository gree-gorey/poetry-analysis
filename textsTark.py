# -*- coding:utf-8 -*-
__author__ = 'Gree-gorey'

import lxml.html
import urllib2
import time
import codecs

t1 = time.time()
n = 0
nextPage = True

urlMain = u'http://search.ruscorpora.ru/search.xml?env=alpha&mode=poetic&sort=gr_created_&text=meta&doc_author=%c0.%20%c0.%20%d2%e0%f0%ea%ee%e2%f1%ea%e8%e9'

while nextPage is True:
    page = urllib2.urlopen(urlMain).read()  # .decode(u'utf-8')
    tree = lxml.html.fromstring(page)
    results = tree.xpath(u'//p[@class="pager"]/a')
    if results[-1].text != u'следующая страница':
        nextPage = False
    urlMain = u'http://search.ruscorpora.ru/' + results[-1].get(u'href')

    results = tree.xpath(u'//li/a')
    for node in results:
        n += 1
        if n < 10:
            N = u'00' + str(n)
        elif n < 100:
            N = u'0' + str(n)
        else:
            N = str(n)
        print N
        name = '/home/gree-gorey/Py/Poetry/Tark1/' + N + '.txt'
        w = codecs.open(name, 'w', 'utf-8')

        url = u'http://search.ruscorpora.ru/' + node.get(u'href')
        page = urllib2.urlopen(url).read()
        tree = lxml.html.fromstring(page)
        results = tree.xpath(u'//li/span[@class="b-wrd-expl"]')
        for node in results:
            w.write(node.text + u'\n')
        w.close()

t2 = time.time()

print t2 - t1
