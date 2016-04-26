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
        key = stationid[1]

        if key.lower() == 'start station id':
                continue

        print '%s\t%s'%(key,1)
