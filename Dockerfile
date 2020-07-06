FROM centos
RUN yum install python3 nginx -y \
        && pip3 install requests bs4
COPY nginx.conf /etc/nginx/nginx.conf
COPY ggle.py /usr/share/nginx/html/ggle/ggle.py
STOPSIGNAL SIGTERM
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
