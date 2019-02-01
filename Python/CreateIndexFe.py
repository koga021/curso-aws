#!/usr/bin/python

import jinja2
import os
import sys

template_filename="/usr/local/curso-aws/Template/IndexFe.html"
rendered_filename="/var/www/html/index.html"


templateLoader = jinja2.FileSystemLoader(searchpath="/usr/local/curso-aws/Template/")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "IndexFe.html"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(name="Minha primeira render")  # this is where to put args to the template renderer

print(outputText)
with open("/var/www/html/index.html", "wb") as fh:
    fh.write(outputText)
