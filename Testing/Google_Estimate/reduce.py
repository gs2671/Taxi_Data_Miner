#!/usr/bin/env python
import sys     
import string

new_key = None
old_key = None
dis_list = []
est_list = []

diff = 0 

for line in sys.stdin:
	line = line.strip()
	keys,value = line.split("\t")
	key, table = keys.split("^")
	new_key = key

	if (not old_key):
		old_key = key
		if (table == 'E'):
			est_list.append('%s'%(value))
		elif(table == 'D'):
			dis_list.append('%s'%(value))

	elif (old_key == new_key):
		if (table == 'E'):
			est_list.append('%s'%(value))
		elif(table == 'D'):
			dis_list.append('%s'%(value))

	elif (old_key != new_key):
		for i in dis_list:
			for j in est_list:
				val1 = j.split(',')
				val2 = i.split(',')
				diff = int(val2[0])-int(val1[0])
				print '%s\t%s\t%s'%(val1[1],val2[1],diff)
		est_list = []
		dis_list = []
		old_key = new_key
		if (table == 'E'):
			est_list.append('%s'%(value))
		elif(table == 'D'):
			dis_list.append('%s'%(value))

for i in dis_list:
	for j in est_list:
		val1 = j.split(',')
		val2 = i.split(',')
		diff = int(val2[0])-int(val1[0])
		print '%s\t%s\t%s'%(val1[1],val2[1],diff)
est_list = []
dis_list = []
