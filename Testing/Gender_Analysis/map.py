#!/usr/bin/env python
import sys    

for line in sys.stdin:
        #default value
        key = 0
        line = line.strip()
        tmp = line.split(",")

        time = tmp[1]
        time = time.strip('"')
        gen = tmp[14]
        gen = gen.strip('"')
        if time != 'starttime' and gen != 'gender' :
                year,mon,day = time.split("-")
                mon = int(mon[:2])
                print '%s,%s\t%s'%(gen,mon,1)

