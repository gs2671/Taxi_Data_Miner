import requests
import zipfile
import os

url = 'https://s3.amazonaws.com/tripdata/{}{}-citibike-tripdata.zip'
# https://s3.amazonaws.com/tripdata/201401-citibike-tripdata.zip


# Download the data for all 12 month for the year 2014
for j in range(1, 13):
    i = "%02d" % j
    print (i)
    r = requests.get(url.format('2014', i), stream = True)
    
    with open('CitiBike/{}_{}_tripdata.zip'.format('2014',i), 'wb') as f:
        for bulks in r.iter_content(chunk_size=1024):
            if bulks:
                f.write(bulks)
    f.close()

    zip_ref = zipfile.ZipFile('CitiBike/{}_{}_tripdata.zip'.format('2014',i), 'r')
    zip_ref.extractall('CitiBike')
    zip_ref.close()

    if int(i) < 9:
        os.rename('CitiBike/{}-{} - Citi Bike trip data.csv'.format('2014',i), 'CitiBike/{}_{}_tripdata.csv'.format('2014',i))
    else:
        os.rename('CitiBike/{}{}-citibike-tripdata.csv'.format('2014',i), 'CitiBike/{}_{}_tripdata.csv'.format('2014',i))
    os.remove('CitiBike/{}_{}_tripdata.zip'.format('2014',i))


# Download the data for all 12 month for the year 2015
for j in range(1, 13):
    i = "%02d" % j
    print (i)
    r = requests.get(url.format('2015', i), stream = True)
    
    with open('CitiBike/{}_{}_tripdata.zip'.format('2015',i), 'wb') as f:
        for bulks in r.iter_content(chunk_size=1024):
            if bulks:
                f.write(bulks)
    f.close()

    zip_ref = zipfile.ZipFile('CitiBike/{}_{}_tripdata.zip'.format('2015',i), 'r')
    zip_ref.extractall('CitiBike')
    zip_ref.close()
    
    os.rename('CitiBike/{}{}-citibike-tripdata.csv'.format('2015',i), 'CitiBike/{}_{}_tripdata.csv'.format('2015',i))
    os.remove('CitiBike/{}_{}_tripdata.zip'.format('2015',i))


