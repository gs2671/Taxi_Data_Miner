#!/usr/bin/env python
import sys    

for line in sys.stdin:
        #default value
        key = 0
        line = line.strip()
        tmp = line.split(",")

        bikeid = tmp[11]
        duration = tmp[0]

        bikeid = bikeid.strip('"')
        duration = duration.strip('"')

        if bikeid != 'bikeid' and duration != 'tripduration' :
                print '%s\t%s'%(bikeid,duration)

