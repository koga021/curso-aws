#!/bin/sh
sudo su -
apt-get update
cd /usr/local
git clone https://github.com/koga021/curso-aws.git
cd curso-aws
apt-get install nginx -y
apt-get install python-pip -y

pip install tornado
