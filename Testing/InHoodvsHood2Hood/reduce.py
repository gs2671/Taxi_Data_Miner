#!/usr/bin/env python
import sys
#input comes from STDIN (stream data that goes to the program)
prev_key=None
total=0
inhood=0
outputfile=open('C:\Users\guru316\GITHub\Taxi_Data_Miner\Testing\InHoodvsHood2Hood\Output\\NeihghbourhoodFinal.csv','w')
#for line in open('C:\Users\guru316\GITHub\Taxi_Data_Miner\Testing\InHoodvsHood2Hood\Output\\NeihghbourhoodReduce.csv','r').readlines():
for line in sys.stdin:
    line=line.strip()
    key,value=line.split('|')
    if(prev_key==None):
        prev_key=key
    if(prev_key!=key):
        str= "%s\t%d\t%d\n" % (prev_key,inhood,total)
        print str
        #outputfile.write(str)
        prev_key=key
        inhood=0
        total=0
    inh,tot=value.split(',')
    inhood+=int(inh)
    total+=int(tot)
str= "%s\t%d\t%d\n" % (prev_key,inhood,total)
#outputfile.write(str)
print str