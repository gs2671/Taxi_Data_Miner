import requests
import os
import time
import pandas as p


def read_data(file_name):

    file = file_name+'.csv'
    data_frame = p.read_csv(file)

    #check the whether each file(day) has 24 hours
    try:
        data_frame['Hour'] = data_frame['TimeEST'].map(lambda x: time.strptime(x, "%I:%M %p").tm_hour)
    except:
        data_frame['Hour'] = data_frame['TimeEDT'].map(lambda x: time.strptime(x, "%I:%M %p").tm_hour)
    data_frame['hourly'] = data_frame['Hour'].map(lambda x: file_name[8:]+'_'+str(x).zfill(2))
    data_frame = data_frame[['hourly', 'TemperatureF','Wind SpeedMPH','Conditions',]]
    #remove dupdiacte if exists
    try:
        data_frame = data_frame.drop_duplicates()
    except:
        pass
    data_frame = data_frame.set_index('hourly')
    return data_frame



def get_weather_data(url):
    for i in range(1, 13):
        i = '%02d'%i
        for j in range(1, 32):
            j = '%02d'%j
            #weather data for 2014
            r = requests.get(url.format('2014',i, j))
            data = r.text
            with open('rawdata/{}_{}_{}.csv'.format('2014',i, j), 'wb') as f:
                f.write(data)
                f.close()
            print '{}-{}'.format('2014',i)

            #weather data for 2015
            r = requests.get(url.format('2015', i, j))
            data = r.text
            with open('rawdata/{}_{}_{}.csv'.format('2015', i, j), 'wb') as f:
                f.write(data)
                f.close()
            print '{}-{}'.format('2015',i)
    print 'Downloaded'


def clean_data():

    for i in range(1, 13):
        i='%02d'%i
        for j in range(1, 32):
            j='%02d'%j
            file_name = 'rawdata/2014_'+str(i)+'_'+str(j)
            data_frame = read_data(file_name)
            data_frame.to_csv('rawdata/C_'+'2014_'+str(i)+'_'+str(j)+'.csv', sep=',')

    for i in range(1, 13):
        i='%02d'%i
        for j in range(1, 32):
            j='%02d'%j
            file_name = 'rawdata/2015_'+str(i)+'_'+str(j)
            data_frame = read_data(file_name)
            data_frame.to_csv('rawdata/C_'+'2015_'+str(i)+'_'+str(j)+'.csv', sep=',')

    print 'Cleaned'

def agg_file():
    year14 = open("weather_2014.csv",'a')

    for i in range(1, 13):
        i='%02d'%i
        for j in range(1, 32):
            j='%02d'%j
            try:
                file1 = 'rawdata/C_'+'2014_'+str(i)+'_'+str(j)+'.csv'
                f1 =open(file1)
                f1.next()
                for line in f1:
                    year14.write(line)
                f1.close()
            except:
                pass
    year14.close()
    print ('2014 file completed')

    year15 = open("weather_2015.csv",'a')

    for i in range(1, 13):
        i='%02d'%i
        for j in range(1, 32):
            j='%02d'%j
            try:
                file1 = 'rawdata/C_'+'2015_'+str(i)+'_'+str(j)+'.csv'
                f1 =open(file1)
                f1.next()
                for line in f1:
                    year15.write(line)
                f1.close()
            except:
                pass
    year15.close()
    print ('2015 file completed')

def main():
    url = 'https://www.wunderground.com/history/airport/KNYC/{}/{}/{}/DailyHistory.html?req_city=New+York&req_state=NY&req_statename=New+York&reqdb.zip=10001&reqdb.magic=5&reqdb.wmo=99999&format=1'
    #https://www.wunderground.com/history/airport/KNYC/2016/4/27/DailyHistory.html?req_city=New+York&req_state=NY&req_statename=New+York&reqdb.zip=10001&reqdb.magic=5&reqdb.wmo=99999&format=1
    
    i,j=0,0
    get_weather_data(url)
    clean_data()
    agg_file()
    #os.remove('rawdata')

if __name__=='__main__':main()

