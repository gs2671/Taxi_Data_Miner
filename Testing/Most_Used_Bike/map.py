#!/usr/bin/env python
import sys    

for line in sys.stdin:
        #default value
        key = 0
        line = line.strip()
        tmp = line.split(",")

        if 'bikeid' in line:
                continue

        bikeid = tmp[11]
        duration = tmp[0]
        print '%s\t%s'%(bikeid,duration)

