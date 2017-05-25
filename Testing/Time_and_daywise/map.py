#!/usr/bin/env python
import sys
import os
from datetime import date
import holidays

us_holidays = holidays.UnitedStates()


def checkDateType(year,month,day):
        if date(year, month, day) in us_holidays:
                return -1
        d = date (year,month,day).weekday()
        if d>= 0 and d<5:
                return d
        else:
                return -1


for line in sys.stdin:

	line = line.strip()
	values = line.split(',')
	datetypes = ''

	if 'starttime' in line:
		continue
	_date = values[1][:10]
	_time = values[1][-8:][:2]
	_time = int(_time)

	year,month,day = _date.split('-')
	datetypes = checkDateType(int(year),int(month),int(day))

	if datetypes != -1:
		if _time < 11 and _time >=4:
			key = '{},{}'.format(datetypes,'Morning')
			print '%s\t%s'%(key,1)
		if _time < 15 and _time >=11:
			key = '{},{}'.format(datetypes,'Afternoon')
			print '%s\t%s'%(key,1)
		if _time < 19 and _time >=15:
			key = '{},{}'.format(datetypes,'Evening')
			print '%s\t%s'%(key,1)
		else:
			key = '{},{}'.format(datetypes,'Night')
			print '%s\t%s'%(key,1)


