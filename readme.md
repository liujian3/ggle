# ENV:
   - centos
   - python3(requests bs4)
   - nginx

# Run
- ```docker build -t ggle:v1 . -f Dockerfile```
- ```docker run -d -p 80:80 --name gglex ggle:v1```

# Test
- ```docker exec -it gglex python3 /usr/share/nginx/html/ggle/ggle.py g "key words" 10 0```
- key words, pages default 10(max 100), start default 0
- access to the ```yourip:80/ggle``` and you will see the nginx default web page
