#!/usr/bin/env python
import sys    
import os


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

        if 'distance' in filename:
                try:
                        key = '{},{}^{}'.format(values[0],values[1],'E')
                        items = '{},{}'.format(values[2],values[3][:-2])
                        print '%s\t%s'%(key,items)
                        key = '{},{}^{}'.format(values[1],values[0],'E')
                        items = '{},{}'.format(values[2],values[3][:-2])
                        print '%s\t%s'%(key,items)
                except: 
                        pass


        if 'tripdata' in filename and (values[12].strip('"') == 'Subscriber' or values[12].strip('"') == 'subscriber'):
                try:
                        year = int(values[13].strip('"'))
                        date = values[1].strip('"')[:10]
                        time = int(date.split('-')[2][:4])
                        start_stationid = int(values[3].strip('"'))
                        end_station = int(values[7].strip('"'))
                        age = time-year
                        gender = 'M' if int(values[14].strip('"')) == 1 else 'F'

                        if (start_stationid == 72 or end_station == 72) and age < 35 and age > 25:
                                key = '{},{}^{}'.format(start_stationid,end_station,'D') 
                                items = '{},{}'.format(values[0],gender)
                                print '%s\t%s'%(key,items)
                except:
                        pass




