# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 10:12:21 2020

@author: hp
"""

#Extracting Data from XML

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#opening url
url ='http://py4e-data.dr-chuck.net/comments_758916.xml'
html = urlopen(url, context=ctx).read().decode()

#making tree
tree = ET.fromstring(html)
lst=tree.findall('comments/comment')

#operation
sum=0
for item in lst:
    sum+=int(item.find('count').text) # tree.findall('.//count') to get all count on page
print(sum)
