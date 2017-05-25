#!/usr/bin/env python
import sys    
import calendar
from datetime import  *


for line in sys.stdin:
        #default value
        key = 0
        line = line.strip()
        tmp = line.split(",")

        if 'starttime' in line:
                continue

        #getting days count
        startdate = tmp[1]

        yr,mon,day = startdate.split("-")
        year = int(yr)
        day = int(day[:2])
        mon = int(mon)

        date = datetime(year,mon,day)
        day = calendar.day_name[date.weekday()]
        print '%s\t%d'% (day,1)
       
