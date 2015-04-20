#!/usr/bin/python
# -*- coding: utf-8 -*-

print "Cache-Control:no-store, no-cache, must-revalidate"
print "Content-Type: text/html\n\n"

from jinja2 import Template, Environment, FileSystemLoader
from connection import cursor, db
import cgi, cgitb,Cookie,os
import footer
data = cgi.FieldStorage()
cid = data.getvalue("cid")
title = "Exam Submission"
if 'HTTP_COOKIE' in os.environ:
	cookie_string=os.environ.get('HTTP_COOKIE')
	c=Cookie.SimpleCookie()
	c.load(cookie_string)

templateLoader = FileSystemLoader( searchpath="/" )
templateEnv = Environment( loader=templateLoader )

if c['type'].value == "teacher":
	sql = "SELECT * from exam WHERE course_id = '{0}' and type='code'".format(str(cid)) #line to select assignment and pass to teacher_course page <select> tag
	cursor.execute(sql) 
	exam_list = cursor.fetchall()
	TEMPLATE_FILE = "/var/www/html/teacher/exam_submission.html"
	template = templateEnv.get_template( TEMPLATE_FILE )
	templateVars = { "title" : title,  "cid":cid,"name":c['name'].value, "footer": footer.html, "examlist": exam_list }
	print template.render( templateVars )
else:
	TEMPLATE_FILE = "/var/www/html/redirect.html"
	template = templateEnv.get_template( TEMPLATE_FILE )
	print template.render(  )
