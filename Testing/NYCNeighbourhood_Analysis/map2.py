import sys
from rtree import index
import shapefile

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Polygon:
    def __init__(self,points):
        self.points = points
        self.nvert = len(points)

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

neighbourhoods=[]
idx = index.Index()
sf = shapefile.Reader("C:\Users\guru316\Desktop\DSGA1004BigData\Project\Neighbourhood Information\NewNeighbourhoodInfo\New2\geo_export_1ff2bdaf-18a7-49b0-adad-5426cc1b8186.shp")
shapes = sf.shapeRecords()
for sh in shapes:
    hdrec=sh.record
    hdshp=sh.shape
    hdboro=hdrec[1]
    hdname=hdrec[6]
    hdbbox=hdshp.bbox
    hdpoints=hdshp.points
    idx.insert(len(neighbourhoods),[hdbbox[1],hdbbox[0],hdbbox[3],hdbbox[2]])
    neighbourhoods.append((hdname,hdboro,hdpoints))

#for line in sys.stdin:
for line in open('C:\Users\guru316\Desktop\DSGA1004BigData\\Project\\CitiBike\\Citibike_04Dec15.csv','r').readlines():
    if("start station name" in line):
        continue
    line = line.strip()
    tripduration,starttime,stoptime,startstationid,startstationname,startstationlatitude,startstationlongitude,endstationid,endstationname,endstationlatitude,endstationlongitude,bikeid,usertype,birthyear,gender= line.split(",")
    st_point = Point(float(startstationlatitude),float(startstationlongitude))
    match = idx.intersection((st_point.x,st_point.y,st_point.x,st_point.y))
    print "Hello"
    for a in match:
        print "Hello"