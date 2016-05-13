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


subway_stations=open('C:\Users\guru316\Desktop\DSGA1004BigData\Project\SubwayData\\SubwayStationData.txt','r').readlines()
citibike_stations=open('C:\Users\guru316\Desktop\DSGA1004BigData\Project\CitiBike\\CitibikeStationData.csv','r').readlines()

idx = index.Index()
i=0
for line in citibike_stations:
    line=line.strip()
    stationid,coordinates=line.split('|')
    coordinates=coordinates.strip("[()]")
    lat,long=coordinates.split(',')
    lat=float(lat)
    long=float(long)
    idx.insert(i,(lat,long,lat,long))
    i+=1

subway_dict=dict()
for line in subway_stations:
    line=line.strip()
    coords=[]
    subwaystationname,coordinates=line.split('|')
    coordinates=coordinates.strip("[]")
    coordinates=re.split(r',\s*(?=[^)]*(?:\(|$))', coordinates)
    for t in coordinates:
        t=t.strip("()")
        lat,long=t.split(',')
        coords.append(Point(float(lat),float(long)))
    subway_dict[subwaystationname]=coords

for key, value in d.iteritems():
    poly=Polygon(value)
    results=idx.nearest(1,)
  

