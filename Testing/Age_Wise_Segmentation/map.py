#!/usr/bin/env python
import sys    

for line in sys.stdin:
        #default value
        key = 0
        line = line.strip()
        tmp = line.split(",")

        if 'starttime' in line:
                continue

        #getting fare_amount value
        key = (tmp[13])
        time = tmp[1]

        yr,mon,day = time.split("-")
        year = int(yr)
        if int(key) == 0:
                print '%s\t%s'%('unknown',1)
        else:
                age = year -int(key)
                if age <= 25:
                        print '%s\t%s'%('< 25',1)
                elif age > 25 and age <= 35:
                        print '%s\t%s'%('26 - 35',1)
                elif age > 35 and age <= 45:
                        print '%s\t%s'%('36 - 45',1)
                elif age < 45 and age <= 55:
                        print '%s\t%s'%('46 - 55',1)
                elif age < 55 and age <= 65:
                        print '%s\t%s'%('56 - 65',1)
                elif age < 65 and age <= 75:
                        print '%s\t%s'%('66 - 75',1)
                else:
                        print '%s\t%s'%('>75',1)

