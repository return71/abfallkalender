# -*- coding: utf-8 -*-
'''
Created on 06.03.2017

@author: ralf
'''
from abfall.kalenderparser import KalenderParser
from abfall.abfallical import AbfallIcall
import urllib.request


if __name__ == '__main__':
    data = b'place=K%C3%B6nnern&senden=Suchen'
    url = 'http://www.awb-salzlandkreis.de/kalender/'
    response = urllib.request.urlopen(url, data)
    s = response.read()
#    s = open("results.html").read()

    parser = KalenderParser(s)
    termine = (parser.returnAbfuhrtermine())
    print('Anzahl Termine: ', len(termine))
#    print(termine)
    kalender = AbfallIcall(termine)
#    print(kalender.get_iCal())
    open('abfalltermine.ics', 'w').write(kalender.get_iCal())
