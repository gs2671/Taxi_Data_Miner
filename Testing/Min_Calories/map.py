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
        filename = 'tripdata'

        line = line.strip('\n')
        values = line.split(',')


        if 'start station id' in line or 'start_station_id' in line:
                continue

        if 'tripdata' in filename and (values[12] == 'Subscriber' or values[12] == 'subscriber'):
                try:
                        year = int(values[13])
                        date = values[1][:10] 
                        time = int(date.split('-')[0][:4])
                        age = time-year
                        gender = 'M' if int(values[14]) == 1 else 'F'
                        duration = int(values[0])/60

                        if gender == 'M':
                            calories = ( (age*0.2017) - (180 * 0.09036) + (110*0.6309) - 55.0969) * (duration/ 4.184)
                        else:
                            calories = ( (age*0.074) - (160 * 0.05741) + (100*0.4472) - 20.4022) * (duration/ 4.184)

                        key = '{}'.format(gender) 
                        items = '{}'.format(calories)
                        print '%s\t%s'%(key,items)
                except:
                        pass




