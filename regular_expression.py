# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 21:34:48 2020

@author: sagnav
"""

import re
line="hello 2 world 456 hello 55.55"
y=re.findall('.([0-9.]+)',line) 
print(y)
#greedy and non greedy
line2="from: hello world: great"
if re.search('^f.+?:',line2):
    print('true')
else:
    print('false')

#extracting
y=re.findall('^f.+?:',line2) #if we use greedy then result will be later :
print(y)
 
#checking email address
emailId="jahsh@gmail.com"
if re.search('\S+@\S+$com',emailId):
    print('true')
else:
    print('false')
y=re.findall('@(\S+)',emailId) 
print(y)
 


