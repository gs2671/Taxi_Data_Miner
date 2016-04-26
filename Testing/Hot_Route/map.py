#!/usr/bin/env python
import sys    


for line in sys.stdin:
        #default value
        key = 0
        line = line.strip()
        tmp = line.split(",")

        #getting hot spot station
        stationid = tmp[3]
        stationid = stationid.split('"')
        key1 = stationid[1]

        endstationid = tmp[7]
        endstationid = endstationid.split('"')
        key2 = endstationid[1]

        if key1.lower() == 'start station id':
                continue

        key = key1+':'+key2

        print '%s\t%s'%(key,1)
