import sys
from rtree import index
import time
import csv
import re

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Polygon:
    def __init__(self,points):
        self.points = points
        self.nvert = len(points)
          
    def lowerbound(self):
        lb_lat=99999.99
        lb_lon=99999.99
        for pt in self.points:
            if(pt.x<lb_lat):
                lb_lat=pt.x
            if(pt.y<lb_lon):
                lb_lon=pt.y
        return Point(lb_lat,lb_lon)

    def upperbound(self):
        ub_lat=None
        ub_lon=None
        for pt in self.points:
            if(pt.x>ub_lat):
                ub_lat=pt.x
            if(pt.y>ub_lon):
                ub_lon=pt.y
        return Point(ub_lat,ub_lon)

    def contains(self,pt):
        firstX = self.points[0].x
        firstY = self.points[0].y
        testx = pt.x
        testy = pt.y
        c = False
        j = 0
        i = 1
        nvert = self.nvert
        while (i < nvert) :
            vi = self.points[i]
            vj = self.points[j]

            if(((vi.y > testy) != (vj.y > testy)) and (testx < (vj.x - vi.x) * (testy - vi.y) / (vj.y - vi.y) + vi.x)):
                c = not(c)
            if(vi.x == firstX and vi.y == firstY):
                i = i + 1
                if (i < nvert):
                    vi = self.points[i];
                    firstX = vi.x;
                    firstY = vi.y;
            j = i
            i = i + 1
        return c

resultfile=open('C:\Users\guru316\GITHub\Taxi_Data_Miner\Testing\Subway_Citibike_Analysis\\Subway_CitiBike_Nearest.txt','w')
subway_stations=open('C:\Users\guru316\Desktop\DSGA1004BigData\Project\SubwayData\\SubwayStationData.txt','r').readlines()
citibike_stations=open('C:\Users\guru316\Desktop\DSGA1004BigData\Project\CitiBike\\CitibikeStationData.csv','r').readlines()

citibike_dict=dict()
for line in citibike_stations:
    line=line.strip()
    stationid,coordinates=line.split('|')
    coordinates=coordinates.strip("[()]")
    clat,clong=coordinates.split(',')
    clat=float(clat)
    clong=float(clong)
    citibike_dict[stationid]=Point(clat,clong)
    

subway_dict=dict()
subway_stat_dict=dict()
idx = index.Index()
i=0
for line in subway_stations:
    line=line.strip()
    coords=[]
    subwaystationname,coordinates=line.split('|')
    coordinates=coordinates.strip("[()]")
    slat,slong=coordinates.split(',')
    slat=float(slat)
    slong=float(slong)
    i+=1
    subway_dict[i]=Point(slat,slong)
    subway_stat_dict[i]=subwaystationname
    idx.insert(i,(slat,slong,slat,slong))

resultfile.write("Citibike Station,Citi_Lat,Citi_Long,Subway Station,Sub_Lat,Sub_Long\n")
for key, value in citibike_dict.iteritems():
    results=list(idx.nearest((value.x,value.y,value.x,value.y),1))
    sub=int(results[0])
    resultfile.write("%s,%f,%f,%s,%f,%f\n" %(key,value.x,value.y,subway_stat_dict[sub],subway_dict[sub].x,subway_dict[sub].y))