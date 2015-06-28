#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi,cgitb,connection,Cookie,os
from jinja2 import Template, Environment, FileSystemLoader 
print "Content-Type: text/html\n\n"
templateLoader = FileSystemLoader( searchpath="/" )
templateEnv = Environment( loader=templateLoader )
from mixpanel import Mixpanel
mp = Mixpanel("25fad57ef2b1fbf474516adf5357abf7")
mp.track('page viewed', 'acourse w/0 login');
acourse="select * from courses"
connection.cursor.execute(acourse)
all_courses=connection.cursor.fetchall()
user=""	
TEMPLATE_FILE = "/var/www/html/acourse.html" 
templateVars = { "all_courses":all_courses}
template = templateEnv.get_template( TEMPLATE_FILE )
print template.render(templateVars)
