from geopy.distance import vincenty

lines = open('../../Data/Subway_CitiBike_Nearest.csv')

output = open('../../Results/station-distance.csv', 'w')
output.write('station_id,distance\n')
for line in lines:
    if 'bike' in line:
        continue
    data = line.split(',')
    p1 = (float(data[1]), float(data[2]))
    p2 = (float(data[4]), float(data[5]))
    output.write(('%s,%s\n')%(data[0], vincenty(p1, p2).miles))
