import os
import time
import pandas as p
from dateutil.parser import parse
import math

stationlist = []
def read_data(file_name):

	file = file_name+'.csv'
	data_frame = p.read_csv(file)

	data_frame['tripduration'] = data_frame['tripduration'].map(lambda x: x if int(x) > 60 else 0)
	data_frame['starttime'] = data_frame['starttime'].map(lambda x: parse(x))
	data_frame['stoptime'] = data_frame['stoptime'].map(lambda x: parse(x))
	data_frame['start station latitude'] = data_frame['start station latitude'].map(lambda x: float(x))
	data_frame['end station latitude'] = data_frame['end station latitude'].map(lambda x: float(x))
	data_frame['start station longitude'] = data_frame['start station longitude'].map(lambda x: float(x))
	data_frame['end station longitude'] = data_frame['end station longitude'].map(lambda x: float(x))
	data_frame['birth year'] = data_frame['birth year'].map(lambda x: check(x))
	
	try:
		data_frame = data_frame.drop_duplicates()
	except:
		pass
	data_frame = data_frame.set_index('tripduration')
	return data_frame

def check(x):
	try:
		value = int(x)
		return value
	except:
		return 0 

def clean_data():

	for i in range(1, 13):
		i='%02d'%i
		file_name = '2014_'+str(i)+'_'+'tripdata'
		data_frame = read_data(file_name)
		data_frame.to_csv('cleaned_data/'+'2014_'+str(i)+'_tripdata.csv', sep=',')
		print 'Cleaned: 2014-{}'.format(i)

	for i in range(1, 13):
		i='%02d'%i
		file_name = '2015_'+str(i)+'_'+'tripdata'
		data_frame = read_data(file_name)
		data_frame.to_csv('cleaned_data/'+'2015_'+str(i)+'_tripdata.csv', sep=',')
		print 'Cleaned: 2015-{}'.format(i)

	print 'Cleaned all data'

def main():
	clean_data()

if __name__=='__main__':main()

