#!/usr/bin/env python
import sys    

for line in sys.stdin:
        #default value
        key = 0
        line = line.strip()
        tmp = line.split(",")
        if 'start station id' in line:
                continue
        key = tmp[3]
        print '%s\t%s'%(key,1)
