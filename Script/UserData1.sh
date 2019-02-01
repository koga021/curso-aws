#!/bin/sh
LoadBalancerFe=""
LoadBalancerBe=""
QueueAddress=""


sudo su -
apt-get update -y
cd /usr/local
git clone https://github.com/koga021/curso-aws.git
cd curso-aws
##apt-get install awscli -y
apt-get install nginx -y
apt-get install python-pip -y

pip install tornado
pip install requests
pip install jinja2

python Python/CreateIndexFe.py
#python /usr/local/curso-aws/Python/CreateIndexFe.py
