#!/usr/bin/env python
import sys    
import os
#from operator import itemgetter
weather_list = []

for line in sys.stdin:
    try:
        filename = os.environ['mapreduce_map_input_file']
    except KeyError:
        filename = os.environ['map_input_file']
            
    #default value
    key = ''
    age = 0
    items = ''


    line = line.strip('\n')
    values = line.split(',')


    if 'start station id' in line or 'start_station_id' in line:
        continue

    if 'weather' in filename:
        try:
            key = '{}'.format(values[0])
            items = '{}^{}'.format('W',values[1])
            print '%s\t%s'%(key,items)
        except: 
            pass


    if 'tripdata' in filename:
        try:
            date = values[1].strip('"')[:10]
            day = date[:10].strip()
            month,day,year = day.split('/')
            month = '%02d'%int(month)
            year = year[:4]
            timestamp = year+'_'+month+'_'+day+'_'
            time = values[1].strip('"')[-5:].split(':')[0]
            time = '%02d'%int(time)
            timestamp = timestamp+str(time)
            key = '{}'.format(timestamp)
            items = '{}^{}'.format('T',1)
            print '%s\t%s'%(key,items)
        except:
            pass




