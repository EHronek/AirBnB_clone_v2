#!/usr/bin/env bash
# Setsup your web servers for the deployment of web_static

sudo apt-get -y update ; sudo apt -y update
sudo apt-get -y install nginx

sudo ufw allow "Nginx HTTP"

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
	sudo rm /data/web_static/current
fi
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

#sudo sed -i '/listen 80;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
CONFIG_FILE="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" "$CONFIG_FILE"; then
    sudo sed -i '/server_name _;/a \
    location /hbnb_static/ { \
        alias /data/web_static/current/; \
        index index.html; \
    }' "$CONFIG_FILE"
fi

sudo service nginx restart

