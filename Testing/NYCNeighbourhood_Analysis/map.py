#!/usr/bin/env python
import sys
import json
import fiona
from shapely.geometry import shape,Point
import shapely
shape_collection=fiona.open("C:\Users\guru316\Desktop\DSGA1004BigData\Project\Neighbourhood Information\ZillowNeighborhoods-NY.shp")
for line in open('C:\Users\guru316\GITHub\Taxi_Data_Miner\Data\Citibike\CitiBike\\cleaned_data\\2015_01_tripdata.csv','r').readlines():
    if("start station name" in line):
        continue
    line = line.strip()
    tripduration,starttime,stoptime,startstationid,startstationname,startstationlatitude,startstationlongitude,endstationid,endstationname,endstationlatitude,endstationlongitude,bikeid,usertype,birthyear,gender= line.split(",")
    st_point = Point(float(startstationlongitude),float(startstationlatitude))
    en_point = Point(float(endstationlongitude),float(endstationlatitude))
    st_flag=0
    en_flag=0
    for shape_record in shape_collection:
        shape = shapely.geometry.asShape(shape_record['geometry'])
        minx, miny, maxx, maxy = shape.bounds
        bounding_box = shapely.geometry.box(minx, miny, maxx, maxy)
        if st_flag!=1:
            if bounding_box.contains(st_point):
                if shape.contains(st_point):
                    hd_name=shape_record['properties']
                    st_hdname=hd_name['NAME']
                    st_flag=1
        elif en_flag!=1:
            if bounding_box.contains(en_point):
                if shape.contains(en_point):
                    hd_name=shape_record['properties']
                    en_hdname=hd_name['NAME']
                    en_flag=1
        if st_flag==1 and en_flag==1:
            key=st_hdname+"|"+en_hdname
            print "%s,1" %(key)
            break