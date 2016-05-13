#!/usr/bin/env python
import sys
import matplotlib
matplotlib.use('Agg')
from matplotlib.path import Path
from rtree import index as rtree
import numpy, shapefile, time
import random
import os
from datetime import datetime
from datetime import date

def readNeighborhood(shapeFilename, index, neighborhoods):
    sf = shapefile.Reader(shapeFilename)
    for sr in sf.shapeRecords():
        paths = map(Path, numpy.split(sr.shape.points, sr.shape.parts[1:]))
        bbox = paths[0].get_extents()
        map(bbox.update_from_path, paths[1:])
        index.insert(len(neighborhoods), list(bbox.get_points()[0])+list(bbox.get_points()[1]))
        neighborhoods.append((sr.record[1], paths, sr.record[0]))

    neighborhoods.append(('UNKNOWN', None, 'UNKNOWN'))


index = rtree.Index()
subway_stations = []
readNeighborhood('C:\Users\guru316\Desktop\DSGA1004BigData\Project\SubwayData\\nyctsubwayroutes_100627.shp', index, subway_stations)
print "Hello"
#for line in sys.stdin:
#    if("start station name" in line):
#        continue
#    line = line.strip()
#    tripduration,starttime,stoptime,startstationid,startstationname,startstationlatitude,startstationlongitude,endstationid,endstationname,endstationlatitude,endstationlongitude,bikeid,usertype,birthyear,gender= line.split(",")
#    st_point = float(startstationlongitude),float(startstationlatitude)
#    en_point = float(endstationlongitude),float(endstationlatitude)

#    pickup_neighborhood = findNeighborhood(st_point, index, neighborhoods, 0)
#    dropoff_neighborhood = findNeighborhood(en_point, index, neighborhoods, 0)
#    #print neighborhoods[pickup_neighborhood][0]
                
#    pickupRegion = neighborhoods[pickup_neighborhood][0]
#    pickupMain = neighborhoods[pickup_neighborhood][2]

#    dropoffRegion = neighborhoods[dropoff_neighborhood][0]
#    dropoffMain = neighborhoods[dropoff_neighborhood][2]

#    key="%s,%s" %(pickupRegion,dropoffRegion)
#    print "%s|%s\n" %(key,line)