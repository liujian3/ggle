# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
import urllib
def geturlparam(p):
    x=p.find('?')+1
    return p[:x-1] if x else p,dict([(i.split('=')[0].strip(),i.split('=')[1].strip()) for i in p[x:].split('&') if i.strip()])
if __name__=='__main__':
    url='http://www.google.com/search?q=%e5%be%90%e6%99%93%e4%b8%9c'
    num='10'
    start='0'
    print(sys.argv)
    # test.py url
    print('python xx.py g searchword numitem startitem')
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
    soup=BeautifulSoup(res.content,features="html.parser")
    
    ss=soup.findAll(class_='ZINbbc xpd O9g5cc uUPGi')
    for s in ss:
        try:
            child=next(s.children)
            url=child.a['href']
            url=urllib.parse.unquote(geturlparam(url)[1]['q'])
            child.a['href']=url
            #print(url)
        except Exception:
            pass

    f=open('test.html','w')
    f.write(str(soup))
    f.close()
