#! /usr/bin/python
import sys
m = dict()
for line in sys.stdin:
  k,v = line.split(',')
  m.setdefault(k, 0)
  m[k] = m[k] + int(v)
for k,v in m.items():
  print "{0},{1}".format(k, v)
