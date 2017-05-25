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


    if 'start station id' in line or 'start_station_id' in line or 'Time' in line:
        continue

    if 'Weather' in filename:
        key = '{}^{}'.format(values[0],'W')
        items = '{}'.format(values[1])
        print '%s\t%s'%(key,items)


    if 'tripdata' in filename:
        try:
            date = values[1][:10]
            year,month,day = date.split('-')
            month = '%02d'%int(month)
            day = '%02d'%int(day)
            timestamp = year+'_'+month+'_'+day+'_'
            time = values[1][-8:].split(':')[0]
            time = '%02d'%int(time)
            timestamp = timestamp+str(time)
            key = '{}^{}'.format(timestamp,'T')
            print '%s\t%s'%(key,1)
        except:
            pass




