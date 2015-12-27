# -*- coding:utf-8 -*-
__author__ = 'Gree-gorey'

import lxml.html
import urllib2
import time
import codecs

t1 = time.time()
n = 357
nextPage = True

urlMain = u'http://search1.ruscorpora.ru/search.xml?sort=gr_tagging&out=normal&dpp=50&spd=10&seed=32200&env=alpha&text=meta&mode=poetic&lang=ru&doc_te_header=&doc_t_cyclus=&doc_t_liber=&doc_te_author=&doc_sex=&doc_g_birthday=&doc_l_birthday=&doc_te_original=&doc_g_created=1907&doc_l_created=1989&doc_g_verses=&doc_l_verses=&doc_genre_fi=&doc_language=&doc_meter=&doc_feet=&doc_clausula=&doc_strophe=&doc_gr_strophe=&doc_rhyme=&doc_formula=&doc_extra=&doc_g_crevision=&doc_l_crevision=&p=' + str(n)

while nextPage is True:
    page = urllib2.urlopen(urlMain).read()
    tree = lxml.html.fromstring(page)
    results = tree.xpath(u'//p[@class="pager"]/a')
    if n == 366:
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
        name = u'/home/gree-gorey/Py/Poetry/Corpus/' + N + u'.txt'
        w = codecs.open(name, 'w', 'utf-8')

        url = u'http://search.ruscorpora.ru/' + node.get(u'href')
        page = urllib2.urlopen(url).read()
        tree = lxml.html.fromstring(page)
        results = tree.xpath(u'//li/span[@class="b-wrd-expl"]')
        for node in results:
            w.write(node.text + u'\n')
        w.close()
        break

t2 = time.time()

print t2 - t1
