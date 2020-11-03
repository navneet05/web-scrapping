# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:51:50 2020

@author: hp
"""

import json
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#opening url
url ='http://py4e-data.dr-chuck.net/comments_758917.json'
html = urlopen(url, context=ctx).read().decode()

#into json
data=json.loads(html)
#operation
numberList=list()
numberList1=list()
numberList=data['comments']
for i in numberList:
    numberList1.append(int(i['count']))
print(sum(numberList1))