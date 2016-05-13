#!/usr/bin/env python
import sys
#input comes from STDIN (stream data that goes to the program)
prev_key=None
count=0
outputfile=open('C:\Users\guru316\GITHub\Taxi_Data_Miner\Testing\Hood2HoodOverTime\Output\\NeihghbourhoodFinal.csv','w')
for line in open('C:\Users\guru316\GITHub\Taxi_Data_Miner\Testing\Hood2HoodOverTime\Output\\NeihghbourhoodReduce.csv','r').readlines():
#for line in sys.stdin:
    line=line.strip()
    key,value=line.split(',')
    if(prev_key==None):
        prev_key=key
    if(prev_key!=key):
        str= "%s\t%d\n" % (prev_key,count)
        #print str
        outputfile.write(str)
        prev_key=key
        count=0
    count+=1
str= "%s\t%d\n" % (prev_key,count)
outputfile.write(str)