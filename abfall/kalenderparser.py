# -*- coding: utf-8 -*-
'''
Created on 06.03.2017

@author: ralf
'''
import os.path
from lxml import html
import datetime

#http://www.awb-salzlandkreis.de/bilder/tonne_schwarz.gif
#http://www.awb-salzlandkreis.de/bilder/tonne_braun.gif
#http://www.awb-salzlandkreis.de/bilder/tonne_blau.gif
#http://www.awb-salzlandkreis.de/bilder/tonne_gelb.gif
#http://www.awb-salzlandkreis.de/bilder/tonne_schwarz_braun.gif
#http://www.awb-salzlandkreis.de/bilder/tonne_schwarz_blau_braun.gif
#http://www.awb-salzlandkreis.de/bilder/tonne_schwarz_blau_gelb_braun.gif
#http://www.awb-salzlandkreis.de/bilder/tonne_blau_gelb.gif

class KalenderParser():
    '''
    parst die Tabellen vom Abfallkalender
    '''
    
    def __init__(self, seite):
        self.seite = seite
        self.Muelltonnen = {'tonne_schwarz': 'Muell',
                            'tonne_braun': 'Bio',
                            'tonne_blau': 'Papier',
                            'tonne_gelb': 'Plaste',
                            'tonne_schwarz_braun': 'Muell, Bio',
                            'tonne_schwarz_blau_braun': 'Muell, Bio, Papier',
                            'tonne_schwarz_blau_gelb_braun': 'Muell, Bio, Plaste, Papier',
                            'tonne_blau_gelb': 'Papier, Plaste'
        }
        
    def returnAbfuhrtermine(self):
        result = []
        tree = html.fromstring(self.seite)
        for tabelle in range(1,13):
            tagcounter = 0
            for zeile in range(2,8):
                for spalte in range(1,8):
                    s = '/html/body/div/div[%s]/table/tr[%s]/td[%s]'%(tabelle, zeile, spalte)
                    element = tree.xpath(s)
                    #print(element)
                    if len(element) > 0:
                        element = element[0]
                        element_text = element.text.lstrip().rstrip()
                        if len(element_text) > 0:
                            tagcounter +=1;
                            #print(element.text.lstrip().rstrip(), tabelle, zeile, spalte, tagcounter)
                        if len(element) > 0:
                            tagcounter +=1
                            tonne = element[0].get('src')
                            tonne = tonne.split('/')
                            tonne =os.path.splitext(tonne[-1:][0])[0]
                            tonne = self.Muelltonnen[tonne]
                            year = datetime.date.today().year
                            datum = datetime.date(year, tabelle, tagcounter)
                            #datum = str(tagcounter) + '.' + str(tabelle) + '.' + str(year) 
                            result.append((tonne, datum ))
                            #print( tonne, tabelle, tagcounter)
        return result
        
    
