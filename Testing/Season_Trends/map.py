#!/usr/bin/env python
import sys

for line in sys.stdin:

	line = line.strip()
	splits = line.split(',')

	day = splits[1]
	day = day.split('"')
	day = day[1]
	if day.lower() == 'starttime':
		continue
	if day:
		month,day,year = day.split('-') 
		year = year[:4]

	tmp = int(month)
	if tmp <= 4 and tmp >= 3:
		print '%s'% ('Spring')
	elif tmp <= 8 and tmp >= 5:
		print '%s'% ('Summer')
	elif tmp <= 11 and tmp >= 9:
		print '%s'% ('Fall')
	else:
		print '%s'% ('Winter')
