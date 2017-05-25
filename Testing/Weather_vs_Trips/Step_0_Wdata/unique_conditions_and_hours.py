import os
import time
import pandas as p



def read_data(file_name):

    file = file_name+'.csv'
    data_frame = p.read_csv(file)
    data_frame = data_frame[['Time','Conditions',]]

    #remove dupdiacte if exists
    try:
        data_frame = data_frame.drop_duplicates()
    except:
        pass
    data_frame = data_frame.set_index('Time')
    return data_frame


def main():
    file = 'weather_2015'
    data_frame = read_data(file)
    data_frame.to_csv('2015_Weather_Condition.csv', sep=',')
    file = 'weather_2014'
    data_frame = read_data(file)
    data_frame.to_csv('2014_Weather_Condition.csv', sep=',')

if __name__=='__main__':main()