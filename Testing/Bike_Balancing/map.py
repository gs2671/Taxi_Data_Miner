#!/usr/bin/env python
import sys    

for line in sys.stdin:
        #default value
        key = 0
        line = line.strip()
        tmp = line.split(",")
        if 'start station id' in line:
                continue
        key = int(tmp[7])

        #317 for E 6 St & Avenue B - East Village
        #460 for S 4 St & Wythe Ave - Queens 
        #if key == 2006:
	date = tmp[2][:10]
        key = '{}:{}'.format(date,key)
	print '%s\t%s'%(key,1)
