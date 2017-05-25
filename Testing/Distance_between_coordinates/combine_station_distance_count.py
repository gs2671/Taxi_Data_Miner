distances = open('../../Results/station-distance.csv')
counts = open('../Trips_on_stationID/ans/part-00000')

output = open('../../Results/station-distance-count.csv','w')
output.write('distance_range,count\n')
station_dict = {}

def get_range(distance):
    distance = float(distance)
    if distance>=0 and distance<=0.1:
        return '0.0 - 0.1'
    elif distance > 0.1 and distance<=0.2:
        return '0.1 - 0.2'
    elif distance > 0.2 and distance<=0.3:
        return '0.2 - 0.3'
    elif distance > 0.3 and distance<=0.4:
        return '0.3 - 0.4'
    elif distance > 0.4 and distance<=0.5:
        return '0.4 - 0.5'
    elif distance > 0.5 and distance<=0.6:
        return '0.5 - 0.6'
    elif distance > 0.6 and distance<=0.7:
        return '0.6 - 0.7'
    elif distance > 0.7 and distance<=0.8:
        return '0.7 - 0.8'
    elif distance > 0.8 and distance<=0.9:
        return '0.8 - 0.9'
    elif distance > 0.9 and distance<=1.0:
        return '0.9 - 1.0'
    elif distance > 1.0 and distance<=1.1:
        return '1.0 - 1.1'
    elif distance > 1.1 and distance<=1.2:
        return '1.1 - 1.2'

distance_dict = {}

min_distance = 100
max_distance = 0
for line in distances:
    if 'distance' in line:
        continue
    station_dict[line.strip().split(',')[0]] = line.strip().split(',')[1]
    if min_distance>float(line.strip().split(',')[1]):
        min_distance = float(line.strip().split(',')[1])
    if max_distance<float(line.strip().split(',')[1]):
        max_distance = float(line.strip().split(',')[1])
print min_distance
print max_distance

for line in counts:
    if 'station_id' in line:
        continue
    data = line.strip().split(',')
    if data[0] in station_dict:
        range_str = get_range(station_dict[data[0]])
        if  range_str in distance_dict:
            distance_dict[range_str] += int(data[1])
        else:
            distance_dict[range_str] = int(data[1])

print distance_dict

output.write('0.0 - 0.1,%s\n'%(distance_dict.get('0.0 - 0.1',0)))
output.write('0.1 - 0.2,%s\n'%(distance_dict.get('0.1 - 0.2',0)))
output.write('0.2 - 0.3,%s\n'%(distance_dict.get('0.2 - 0.3',0)))
output.write('0.3 - 0.4,%s\n'%(distance_dict.get('0.3 - 0.4',0)))
output.write('0.4 - 0.5,%s\n'%(distance_dict.get('0.4 - 0.5',0)))
output.write('0.5 - 0.6,%s\n'%(distance_dict.get('0.5 - 0.6',0)))
output.write('0.6 - 0.7,%s\n'%(distance_dict.get('0.6 - 0.7',0)))
output.write('0.7 - 0.8,%s\n'%(distance_dict.get('0.7 - 0.8',0)))
output.write('0.8 - 0.9,%s\n'%(distance_dict.get('0.8 - 0.9',0)))
output.write('0.9 - 1.0,%s\n'%(distance_dict.get('0.9 - 1.0',0)))
output.write('1.0 - 1.1,%s\n'%(distance_dict.get('1.0 - 1.1',0)))
output.write('1.1 - 1.2,%s\n'%(distance_dict.get('1.1 - 1.2',0)))
# print distance_dict
# distance_keys = distance_dict.keys()
# distance_keys 
# for item in sorted(distance_keys):
#     output.write('%s,%s\n'%(item, distance_dict[item]))
