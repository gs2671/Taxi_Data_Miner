import json
from shapely.geometry import shape,Point

print "Hello"
with open('NeighborhoodTabulationAreas.geojson', 'r') as f:
    js=json.load(f)

longitude=-73.98887606054689
latitude=40.633174404308775

point = Point(longitude,latitude)

for feature in js['features']:
    polygon=shape(feature['geometry'])
    if polygon.contains(point):
        temp=feature['properties']
        print temp['ntaname']