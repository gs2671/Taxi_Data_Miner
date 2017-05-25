#!/usr/bin/env python
import sys

for line in sys.stdin:

	line = line.strip()
	splits = line.split(',')

	if 'starttime' in line:
		continue

	stationid = splits[7]
	print '%s\t%s'%(stationid,1)