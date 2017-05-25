#!/usr/bin/env python
import sys    

for line in sys.stdin:
        #default value
        key = 0
        line = line.strip()
        tmp = line.split(",")
        if 'start station id' in line:
                continue
        key = int(tmp[3])

        if key == 317:
        	date = tmp[1][-8:]
        	time = int(date.split(':')[0])
        	print '%s\t%s'%(time,1)
