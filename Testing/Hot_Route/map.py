#!/usr/bin/env python
import sys    


for line in sys.stdin:
        #default value
        key = 0
        line = line.strip()
        tmp = line.split(",")

        if 'start station id' in line:
                continue
        #getting hot spot station
        key1 = tmp[3]
        key2 = tmp[7]
        key = key1+':'+key2

        print '%s\t%s'%(key,1)
