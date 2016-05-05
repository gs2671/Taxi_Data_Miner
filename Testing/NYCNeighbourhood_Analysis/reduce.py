#!/usr/bin/env python
import sys
#input comes from STDIN (stream data that goes to the program)
#for line in open('C:\Users\guru316\Desktop\DSGA1004BigData\\Project\\CitiBike\\Citibike_04Dec15_reduce.csv','r').readlines():
prev_key=None
count=0
for line in sys.stdin:
    line=line.strip()
    key,value=line.split(',')
    if(prev_key==None):
        prev_key=key
    elif(prev_key!=key):
        print "%s\t%d" % (prev_key,count)
        prev_key=key
        count=0
    count+=1
print "%s\t%d" % (prev_key,count)