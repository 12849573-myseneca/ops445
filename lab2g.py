#!/usr/bin/env python3

Author: smuhwezi
Program name: lab2g.py
Date Created: September 2023

import sys

if len(sys.argv)>1:
   timer=int(sys.argv[1])
else:
   timer=3

while(timer>0):
  print(timer)
  timer-=1
print('blast off!')
