# ENV:
   - centos
   - python3(requests bs4)
   - nginx

# Run
- ```git clone https://github.com/liujian3/ggle.git && cd ggle```
- ```docker build -t ggle:v1 . -f Dockerfile```
- ```docker run -d -p 80:80 --name gglex ggle:v1```

# Test
- ```docker exec -it gglex python3 /usr/share/nginx/html/ggle/ggle.py web "key words" 10 0```
- source web/news/photo, key words, pages default 10(max 100), start default 0
- access to the ```yourip:80/ggle/test.html``` and you will see the nginx default web page
