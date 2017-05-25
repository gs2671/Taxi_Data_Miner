#!/usr/bin/env python
import sys
import os

for line in sys.stdin:
        try:
                filename = os.environ['mapreduce_map_input_file']
        except KeyError:
                filename = os.environ['map_input_file']
        line = line.strip()
        values = line.split('\t')
        #filename = 'pick'

        if 'pick' in filename:
                print '%s\t%s^%s'%(values[0].strip(' '),'P',values[1].strip(' '))
        if 'drop' in filename:
                print '%s\t%s^%s'%(values[0].strip(' '),'D',values[1].strip(' '))
