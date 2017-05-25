#!/usr/bin/env python
import sys     
import string

old_key = None
new_key = None
old_value = 0
count = 0


for line in sys.stdin:
	line = line.strip()
	key,value = line.split("\t")
	new_key = key
	value = int(value)

	if (not old_key):
		old_key = key
		old_value = value
		count = 1

	elif (old_key == new_key):	
		old_value = old_value + value
		old_key = new_key
		count +=1


	elif (old_key != new_key):
		if old_value > 0:
			i = old_value/count
		else:
			val = abs(old_value)/count
			i = '-{}'.format(val)
		print '%s\t%d'%(old_key,old_value)
		count = 1
		old_value = value
		old_key = new_key
		
if old_value > 0:
	i = old_value/count
else:
	val = abs(old_value)/count
	i = '-{}'.format(val)
print '%s\t%d'%(old_key,old_value)

