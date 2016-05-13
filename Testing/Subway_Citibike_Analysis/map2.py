import sys
print "Reading Subway"
subway_stations=dict()
subway_file=open('C:\Users\guru316\Desktop\DSGA1004BigData\Project\SubwayData\\StationEntrances.csv','r')
for line in subway_file.readlines():
    if "Station_Name" in line:
        continue
    Division,Line,Station_Name,Station_Latitude,Station_Longitude,Route_1,Route_2,Route_3,Route_4,Route_5,Route_6,Route_7,Route_8,Route_9,Route_10,Route_11,Entrance_Type,Entry,Exit_Only,Vending,Staffing,Staff_Hours,ADA,ADA_Notes,Free_Crossover,North_South_Street,East_West_Street,Corner,Latitude,Longitude=line.split(',')
    if(Station_Name not in subway_stations):
        subway_stations[Station_Name]=[(float(Station_Latitude),float(Station_Longitude))]
        #subway_stations[Station_Name].append((float(Latitude),float(Longitude)))
    #else:
    #    subway_stations[Station_Name]=[(float(Latitude),float(Longitude))]
with open('C:\Users\guru316\Desktop\DSGA1004BigData\Project\SubwayData\\SubwayStationData.txt','w') as f:
    [f.write('{0}|{1}\n'.format(key, value)) for key, value in subway_stations.items()]

print "Subway Finished"
print "Reading Citibike Stations"
citibike_stations=dict()
citibike_file=open('C:\Users\guru316\Desktop\DSGA1004BigData\Project\CitiBike\\201512-citibike-tripdata.csv','r')
for line in citibike_file.readlines():
    if("start station name" in line):
        continue
    tripduration,starttime,stoptime,startstationid,startstationname,startstationlatitude,startstationlongitude,endstationid,endstationname,endstationlatitude,endstationlongitude,bikeid,usertype,birthyear,gender=line.split(',')
    if(startstationid not in subway_stations):
        citibike_stations[startstationid]=[(float(startstationlatitude),float(startstationlongitude))]
    elif(endstationid not in subway_stations):
        citibike_stations[endstationid]=(float(endstationlatitude),float(endstationlongitude))
with open('C:\Users\guru316\Desktop\DSGA1004BigData\Project\CitiBike\\CitibikeStationData.csv','w') as f:
    [f.write('{0}|{1}\n'.format(key, value)) for key, value in citibike_stations.items()]
print "Citibike fininshed"
