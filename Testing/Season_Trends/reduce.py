#!/usr/bin/env python
import sys
import string

summer, winter, spring, fall = 0,0,0,0

for line in sys.stdin:

	line = line.strip()

	word = line.lower()

	if word == 'summer':
		summer +=1
	elif word == 'winter':
		winter +=1
	elif word == 'fall':
		fall +=1
	elif word == 'spring':
		spring +=1

print '%s\t%s'%('Summer', summer)
print '%s\t%s'%('Winter', winter)
print '%s\t%s'%('Spring', spring)
print '%s\t%s'%('Fall', fall)
