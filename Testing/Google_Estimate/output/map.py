#!/usr/bin/env python
import sys    


for line in sys.stdin:
        #default value
        key = 0
        line = line.strip()
        tmp = line.split("\t")
        try:
                key = '{},{}'.format(tmp[0].strip(' '),tmp[1].strip(' '))
                item = tmp[2].strip(' ')
                print '%s\t%s'%(key,item)
        except:
                pass
