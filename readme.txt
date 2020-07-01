docker run -itd -p 80:80 --name centosx centos
docker exec -it centosx /bin/bash

yum install vim wget -y
yum install python3 -y
yum install git -y
yum install nginx -y
pip3 install requests bs4 gevent

git config --global user.name "liujian3"
git config --global user.email "liujian3@gmail.com"
cd /usr/share/nginx/html
git clone https://liujian3:Tong11234%2c.%2f@github.com/liujian3/ggle.git
cd test
git pull origin master

mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default1.conf
cat /etc/nginx/conf.d/default1.conf | head -n 10 > /etc/nginx/conf.d/default.conf
echo '        autoindex on;' >> /etc/nginx/conf.d/default.conf
echo '        autoindex_exact_size off;' >> /etc/nginx/conf.d/default.conf
cat /etc/nginx/conf.d/default1.conf | tail -n +12 >> /etc/nginx/conf.d/default.conf
nginx

cd /usr/share/nginx/html/ggle/
git pull origin master
python3 ggle.py g 董卿 10 0
