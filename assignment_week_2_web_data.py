# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:05:55 2020

@author: sagnav
"""
import re

file=open('original_ass_week_2.txt')
numList=list()

for line in file:
    line=line.rstrip()
    code=re.findall('[0-9]+',line)
    if len(code) ==0:continue
    for i in code:
        numList.append(float(i))
print(numList)
sum=0
for i in numList:
    sum+=i
print(sum)