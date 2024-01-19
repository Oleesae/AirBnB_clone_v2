#!/usr/bin/env bash
# install and setup nginx web server
sudo apt-get update
sudo apt-get -y install nginx
sudo apt-get -y install ufw
sudo ufw enable
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default
sudo service nginx restart
