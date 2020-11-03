# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:50:54 2020

@author: hp
"""



from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import ssl
import re
import xlsxwriter

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#user agent
req = Request('https://www.netmeds.com/prescriptions', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})

#opening url
html = urlopen(req, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup.findAll("div", {"class": "prescriptions_products"})
result1=str(tags)

# Retrieve all of the anchor tags
soup = BeautifulSoup(result1, "html.parser")
urlList=list()
contentList=list()
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    urlList.append(tag.get('href', None))
    contentList.append(tag.contents[0])
    
#seperating data contentList
Disease_name=list()
numberOfMedicine=list()
for i in range(len(contentList)):
    Disease_name.append(' '.join(map(str,re.findall('\s*(\S+)\s*\(',contentList[i]))))
    numberOfMedicine.append((' '.join(map(str,re.findall('.+\(([0-9]+)\)',contentList[i]) ))))
numberOfMedicine=[int(j) for j in numberOfMedicine] 
#inserting data into exel sheet
workbook = xlsxwriter.Workbook('netmed_medicine_categories.xlsx') 
  
# The workbook object is then used to add new  
# worksheet via the add_worksheet() method. 
worksheet = workbook.add_worksheet() 
  
# Use the worksheet object to write 
# data via the write() method.
#columns 
worksheet.write('A1', 'Disease_name') 
worksheet.write('B1', 'numberOfMedicine') 
worksheet.write('C1', 'URL') 

#entries
row=1
col=0
for j in Disease_name:
     worksheet.write(row, col, j) 
     row+= 1
col=1
row=1
for j in numberOfMedicine:
     worksheet.write(row, col, j) 
     row += 1
col=2
row=1
for j in urlList:
     worksheet.write(row, col, j) 
     row += 1
workbook.close()













