#!/usr/bin/env python3

import json

f1 = open('file7.json')
f2 = open('file8.json')

d1 = f1.read()
d2 = f2.read()

#print (d1)
#print (d2)
j1 = json.loads(d1)
j2 = json.loads(d2)

print (j1)
print (j2)
