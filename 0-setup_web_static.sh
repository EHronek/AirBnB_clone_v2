#!/usr/bin/env bash
# Setsup your web servers for the deployment of web_static

sudo apt-get -y update ; sudo apt -y update
sudo apt-get -y install nginx

nginx_pid=$(pgrep nginx)

if [ -z "$nginx_pid" ]; then
    /etc/init.d/nginx start
fi

sudo ufw allow "Nginx HTTP"

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

 sudo sed -i '/listen 80;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
