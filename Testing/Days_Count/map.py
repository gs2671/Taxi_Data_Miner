#!/usr/bin/env python
import sys    
import calendar
from datetime import  *


for line in sys.stdin:
        #default value
        key = 0
        line = line.strip()
        tmp = line.split(",")

        #getting days count
        startdate = tmp[1]
        startdate = startdate.split('"')
        startdate = startdate[1]

        if startdate.lower() == 'starttime':
                continue

        mon,day,yr = startdate.split("-")
        year = int(yr[:4])
        day = int(day)
        mon = int(mon)

        date = datetime(year,mon,day)
        day = calendar.day_name[date.weekday()]
        print '%s\t%d'% (day,1)
       
