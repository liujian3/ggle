# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
url='http://www.google.com/search?q=%e5%be%90%e6%99%93%e4%b8%9c'
print(sys.argv)
if len(sys.argv)>2:
    url='http://www.google.com/search?q='+sys.argv[2]
elif len(sys.argv)>1:
    url=sys.argv[1]
res=requests.get(url)
soup=BeautifulSoup(res.content)
f=open('test.html','w')
f.write(res.text)
f.close()
