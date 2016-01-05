#! /usr/bin/python
import re
import sys
for line in sys.stdin:
  m = map( lambda x:(x,1), filter( lambda s:len(s) > 0, re.split( '\W+', line ) ) )
  for k,v in m:
    print "{0},{1}".format( k, v )
