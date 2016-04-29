#!/usr/bin/env python
import sys    

for line in sys.stdin:
        #default value
        key = 0
        line = line.strip()
        tmp = line.split("\t")
        print '%s\t%s'%(tmp[0],tmp[1])

