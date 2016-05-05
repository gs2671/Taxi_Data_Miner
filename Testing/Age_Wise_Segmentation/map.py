#!/usr/bin/env python
import sys    

for line in sys.stdin:
        #default value
        key = 0
        line = line.strip()
        tmp = line.split(",")

        #getting fare_amount value
        birthyear = (tmp[13])
        key = birthyear.strip('"')
        time = tmp[1]
        time = time.strip('"')
        if time != 'starttime':
                day,mon,yr = time.split("-")
                year = int(yr[:4])


        if (key == 'birth year' or key == ''):
                pass
        else:        
                print '%d\t%s'%(year - int(key),1)

