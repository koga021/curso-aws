#!/usr/bin/python

import jinja2
import os
import sys
import requests
r = requests.get("http://169.254.169.254/latest/dynamic/instance-identity/document")
response_json = r.json()
region = response_json.get('region')



r = requests.get("http://169.254.169.254/latest/meta-data/hostname")
hostname = r.content

r = requests.get("http://169.254.169.254/latest/meta-data/public-hostname")
public_host = r.content



template_filename="/usr/local/curso-aws/Template/IndexFe.html"
rendered_filename="/var/www/html/index.html"


templateLoader = jinja2.FileSystemLoader(searchpath="/usr/local/curso-aws/Template/")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "IndexFe.html"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(name=region,host=hostname,public_ip=public_host)  # this is where to put args to the template renderer

print(outputText)
with open("/var/www/html/index.html", "wb") as fh:
    fh.write(outputText)
