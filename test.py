# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
import urllib
import traceback
import gevent
def geturl(c,s):
    try:
        child=next(s.children)
        url=child.a['href']
        url=urllib.parse.unquote(geturlparam(url)[1]['q'])
        res=requests.get(url)
        fpth=str(c)+'h.html'
        f=open(fpth,'w')
        f.write(res.content.decode('utf8'))
        f.close()
        child.a['href']=url
        tag=soup.new_tag('a', attrs={'href':'/test/'+fpth})
        tag.append('快照')
        child.append(tag)
        fpth=str(c)+'t.html'
        f=open(fpth,'w')
        ssoup=BeautifulSoup(res.content,features="html.parser")
        f.write(ssoup.text)
        f.close()
        child.a['href']=url
        tag=soup.new_tag('a', attrs={'href':'/test/'+fpth})
        tag.append('文本')
        child.append(tag)
        print(c)
    except Exception:
        traceback.print_exc()
    
def geturlparam(p):
    x=p.find('?')+1
    return p[:x-1] if x else p,dict([(i.split('=')[0].strip(),i.split('=')[1].strip()) for i in p[x:].split('&') if i.strip()])
if __name__=='__main__':
    url='http://www.google.com/search?q=%e5%be%90%e6%99%93%e4%b8%9c'
    num='10'
    start='0'
    print(sys.argv)
    # test.py url
    print('python xx.py g searchword numitem startitem outfile')
    pn=len(sys.argv)
    outfile='test.html'
    if pn==2:
        url=sys.argv[1]
    elif pn>2:
        url='http://www.google.com/search?q='+sys.argv[2]
        try:
            url+='&num='+sys.argv[3]
            url+='&start='+sys.argv[4]
            outfile=sys.argv[5]
        except Exception:
            pass

    res=requests.get(url)
    soup=BeautifulSoup(res.content,features="html.parser")
    
    ss=soup.findAll(class_='ZINbbc xpd O9g5cc uUPGi')
    c=0
    gs=[]
    for s in ss:
        gs.append(gevent.spawn(geturl,c,s))
        c+=1
        print(c)
    gevent.joinall(gs)
    f=open(outfile,'w')
    f.write(str(soup))
    f.close()
