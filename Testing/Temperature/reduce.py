#!/usr/bin/env python
import sys     
import string

new_key = None
old_key = None
trip_list = []
weather_list = []


for line in sys.stdin:
	line = line.strip()
	keys,value = line.split("\t")
	key, table = keys.split("^")
	new_key = key

	if (not old_key):
		old_key = key
		if (table == 'T'):
			trip_list.append('%s'%(value))
		elif(table == 'W'):
			weather_list.append('%s'%(value))

	elif (old_key == new_key):
		if (table == 'T'):
			trip_list.append('%s'%(value))
		elif(table == 'W'):
			weather_list.append('%s'%(value))

	elif (old_key != new_key):
		types = len(weather_list)
		trips = len(trip_list)
		for i in weather_list:
			print '%s\t%s'%(i,trips)
		trip_list = []
		weather_list = []
		old_key = new_key
		if (table == 'T'):
			trip_list.append('%s'%(value))
		elif(table == 'W'):
			weather_list.append('%s'%(value))

types = len(weather_list)
trips = len(trip_list)
for i in weather_list:
	print '%s\t%s'%(i,trips)
trip_list = []
weather_list = []
