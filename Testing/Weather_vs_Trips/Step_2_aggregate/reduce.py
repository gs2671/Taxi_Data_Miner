#!/usr/bin/env python
import sys     
import string

old_key = None
new_key = None
old_value = 0


for line in sys.stdin:
	line = line.strip()
	key,value = line.split("\t")
	new_key = key
	value = int(value)

	if (not old_key):
		old_key = key
		old_value = value

	elif (old_key == new_key):	
		old_value = old_value +value
		old_key = new_key


	elif (old_key != new_key):
		print '%s\t%d'%(old_key,old_value)
		old_value = value
		old_key = new_key
print '%s\t%d'%(old_key,old_value)

