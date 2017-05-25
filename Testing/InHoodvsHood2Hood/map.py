#!/usr/bin/env python
import sys
#shape_collection=fiona.open("C:\Users\guru316\Desktop\DSGA1004BigData\Project\Neighbourhood Information\ZillowNeighborhoods-NY.shp")
reduce_file=open('C:\Users\guru316\GITHub\Taxi_Data_Miner\Testing\InHoodvsHood2Hood\Output\\NeihghbourhoodReduce.csv','w') 
#for line in sys.stdin:
for line in open('C:\Users\guru316\Desktop\DSGA1004BigData\Project\CitiBike\\CitiBikeTrip_with_Hood.csv','r').readlines():
    try:
        line = line.strip()
        key,value=line.split('|')
        tripduration,starttime,stoptime,startstationid,startstationname,startstationlatitude,startstationlongitude,endstationid,endstationname,endstationlatitude,endstationlongitude,bikeid,usertype,birthyear,gender= value.split(",")
        pickup_hood,dropoff_hood=key.split(',')
        if(pickup_hood==dropoff_hood):
            value="1,1"
        else:
            value="0,1"
        str= "%s|%s\n" %(pickup_hood,value)
        #reduce_file.write(str)
        print str
    except:
        print line