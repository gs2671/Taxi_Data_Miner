#!/usr/bin/env python
import sys
import os
from datetime import date
import holidays

us_holidays = holidays.UnitedStates()

def checkDateType(year,month,day):
        if date(year, month, day) in us_holidays:
                return "H"
        d = date (year,month,day).weekday()
        if d>= 0 and d<5:
                return "W"
        else:
                return "E"


for line in sys.stdin:
	line = line.strip()
	values = line.split('\t')
	datetypes = ''

	_date = values[0].split(':')[0]
	year,month,day = _date.split('-')
	datetypes = checkDateType(int(year),int(month),int(day))
	stationid = values[0].split(':')[1]
	val = values[1]

	key = '{}^{}'.format(datetypes,stationid)
	print '%s\t%s'%(key,val)
