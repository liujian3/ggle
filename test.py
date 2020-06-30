# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
url='http://www.google.com/search?q=%e5%be%90%e6%99%93%e4%b8%9c'
num='10'
start='0'
print(sys.argv)
# test.py url
# test.py g searchword num start
pn=len(sys.argv)
if pn==2:
    url=sys.argv[1]
elif pn>2:
    url='http://www.google.com/search?q='+sys.argv[2]
    try:
        url+='&num='+sys.argv[3]
        url+='&start='+sys.argv[4]
    except Exception:
        pass

res=requests.get(url)
soup=BeautifulSoup(res.content)
f=open('test.html','w')
f.write(res.text)
f.close()
