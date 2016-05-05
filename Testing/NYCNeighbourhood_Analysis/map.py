#!/usr/bin/env python
import sys
import json
from shapely.geometry import shape,Point
#target = open('C:\Users\guru316\Desktop\DSGA1004BigData\\Project\\CitiBike\\Citibike_04Dec15_reduce.csv', 'w')
with open('hooddata', 'r') as f:
#with open('C:\Users\guru316\GITHub\Taxi_Data_Miner\Testing\NYCNeighbourhood_Analysis\NeighborhoodTabulationAreas.geojson', 'r') as f:
    js=json.load(f)
#for line in open('C:\Users\guru316\Desktop\DSGA1004BigData\\Project\\CitiBike\\Citibike_04Dec15.csv','r').readlines():
for line in sys.stdin:
    if("start station name" in line):
        continue
    line = line.strip()
    tripduration,starttime,stoptime,startstationid,startstationname,startstationlatitude,startstationlongitude,endstationid,endstationname,endstationlatitude,endstationlongitude,bikeid,usertype,birthyear,gender= line.split(",")
    #print("%s,%s"%(key,1))
    st_point = Point(float(startstationlongitude),float(startstationlatitude))
    en_point = Point(float(endstationlongitude),float(endstationlatitude))
    st_flag=0
    en_flag=0
    for feature in js['features']:
        polygon=shape(feature['geometry'])
        if st_flag!=1 and polygon.contains(st_point):
            temp=feature['properties']
            st_hdname=temp['ntaname']          
            st_flag=1
        elif en_flag!=1 and polygon.contains(en_point):
            temp=feature['properties']
            en_hdname=temp['ntaname']
            en_flag=1
        if st_flag==1 and en_flag==1:
            key=st_hdname+"|"+en_hdname
            print "%s,1" %(key)
            break;