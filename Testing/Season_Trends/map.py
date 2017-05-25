#!/usr/bin/env python
import sys

for line in sys.stdin:

	line = line.strip()
	splits = line.split(',')

	if 'starttime' in line:
		continue

	day = splits[1]
	year,month,dat = day.split('-') 
	tmp = int(month)
	if tmp <= 4 and tmp >= 3:
		print '%s'% ('Spring')
	elif tmp <= 8 and tmp >= 5:
		print '%s'% ('Summer')
	elif tmp <= 11 and tmp >= 9:
		print '%s'% ('Fall')
	else:
		print '%s'% ('Winter')
