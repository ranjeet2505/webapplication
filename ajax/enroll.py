#!/usr/bin/python
print "Content-Type: text/plain\n\n"

from connection import cursor, db
import cgi, cgitb
import Cookie, os

data = cgi.FieldStorage()
course_id = data.getvalue('course_id')
enroll = data.getvalue('enroll')
#course_id =1
def check_enroll(email_id, course_id):
	sql = "SELECT * FROM enrolled WHERE course_id = '{0}' and email = '{1}'".format(str(course_id), str(email_id))	
	cursor.execute(sql)
	if cursor.rowcount > 0:
		return 1
	else:
		sql = "SELECT * FROM enroll_request WHERE course_id = '{0}' and email_id = '{1}'".format(str(course_id), str(email_id))	
		cursor.execute(sql)
		if cursor.rowcount > 0:
			return 2
		else:
		 	return -1	
#enroll = "true"
if 'HTTP_COOKIE' in os.environ:
	cookie_string=os.environ.get('HTTP_COOKIE')
	c=Cookie.SimpleCookie()
	c.load(cookie_string)
	email_id = c["uid"].value
	if enroll == "true" : 
		if check_enroll(str(email_id), str(course_id)) == -1:
			sql = "INSERT INTO enroll_request(email_id, course_id) VALUES('{0}','{1}')".format(str(email_id),str(course_id))
			cursor.execute(sql)
			db.commit()
			print "Approval Pending"
		else:
			print "Already Enrolled"	
	else:
		status=check_enroll(str(email_id), str(course_id))
		print status

