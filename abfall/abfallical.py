# -*- coding: utf-8 -*-
'''
Created on 07.03.2017

@author: ralf
'''
from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta
import pytz
import uuid


class AbfallIcall(object):
    '''
    rendert die vom KalenderParser empfangenen Daten als iCal File
    '''

    def __init__(self, termine):
        '''
        Constructor
        '''
        self.termine = termine

    def get_iCal(self):
        '''
        gibt den Kalender zurÃ¼ck
        '''
        cal = Calendar()
        cal.add('prodid', '-//Abfall Kalender//keller.inc//')
        cal.add('version', '2.0')

        for termin in self.termine:
            event = Event()
            now = datetime.now(tz=pytz.timezone('Europe/Berlin'))
            event.add('created', now)
            event.add('last-modified', now)
            event.add('dtstamp', now)
            event['uid'] = str(uuid.uuid1())
            event.add('summary', termin[0])
            dtstart = termin[1]
            dtend = dtstart + timedelta(days=1)
            event.add('dtstart', dtstart)
            event.add('dtend', dtend)
            event.add('TRANSP', 'TRANSPARENT')

            alarm = Alarm()
            alarm.add('action', 'DISPLAY')
            alarm.add('trigger', timedelta(days=-1))
            alarm.add('description', termin[0])

            event.add_component(alarm)
            cal.add_component(event)

        result = cal.to_ical(False).decode()
        result = result.replace('\r\n', '\n').strip()
        return result
