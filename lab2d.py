#!/usr/bin/env python3

Author: smuhwezi
Program name: lab2d.py
Date Created: September 2023

import sys
if not len(sys.argv)==3:
   print(f'Usage: {sys.argv[0]} name age')
   sys.exit()

name=sys.argv[1]
age=sys.argv[2]

print('Hi '+name+', you are '+age+' years old.')
