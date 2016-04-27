import urllib2
import urllib
import json
import simplejson

req = urllib2.Request('https://www.citibikenyc.com/stations/json')
opener = urllib2.build_opener()
stationlist = []
lists = []

f= opener.open(req)
json = json.loads(f.read())
for i in json['stationBeanList']:
	tmp = [i['id'],i['latitude'],i['longitude']]
	stationlist.append(tmp)

def getdistance(stationlist):
	for i in stationlist:
		for j in stationlist:
			if int(i[0]) > 72:
				orig_coord = '{},{}'.format(i[1],i[2])
				dest_coord = '{},{}'.format(j[1],j[2])
				url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&mode=bicycling&language=en-EN&sensor=false"%(orig_coord,dest_coord)
				result= simplejson.load(urllib.urlopen(url))
				if result['rows'][0]['elements'][0]['status'] == 'OK':
					driving_time = result['rows'][0]['elements'][0]['duration']['value']
					distance = result['rows'][0]['elements'][0]['distance']['text']
					value = [i[0],j[0],driving_time, distance]
					print value
					lists.append(value)	
	return lists

lists = getdistance(stationlist)
with open ('Station.csv','wb') as f:
	for i in lists:
		val = '{},{},{},{}'.format(i[0],i[1],i[2],i[3])
		f.write(val+'\n')
f.close()


