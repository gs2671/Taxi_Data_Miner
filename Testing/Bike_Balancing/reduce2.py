#!/usr/bin/env python
import sys     
import string

new_key = None
old_key = None
drop_list = []
pick_list = []


for line in sys.stdin:
	line = line.strip()
	key,value = line.split("\t")
	table, value = value.split("^")
	new_key = key
	value = int(value)

	if (not old_key):
		old_key = key
		if (table == 'P'):
			pick_list.append('%d'%(value))
		elif(table == 'D'):
			drop_list.append('%d'%(value))

	elif (old_key == new_key):
		if (table == 'P'):
			pick_list.append('%d'%(value))
		elif(table == 'D'):
			drop_list.append('%d'%(value))

	elif (old_key != new_key):
		if (len(pick_list) > 0 and len(drop_list) > 0):
			i = int(drop_list[0])-int(pick_list[0])
			print '%s\t%s'%(old_key,i)
		elif (len(pick_list) > 0):
			print '%s\t%s'%(old_key,pick_list[0])
		elif (len(drop_list) > 0):
			print '%s\t%s'%(old_key,drop_list[0])

		pick_list = []
		drop_list = []
		old_key = new_key
		if (table == 'P'):
			pick_list.append('%d'%(value))
		elif(table == 'D'):
			drop_list.append('%d'%(value))

if (len(pick_list) > 0 and len(drop_list) > 0):
	i = int(drop_list[0])-int(pick_list[0])
	print '%s\t%s'%(old_key,i)
elif (len(pick_list) > 0):
	print '%s\t%s'%(old_key,pick_list[0])
elif (len(drop_list) > 0):
	print '%s\t%s'%(old_key,drop_list[0])

