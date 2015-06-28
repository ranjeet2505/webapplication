#!/usr/bin/python
import json
print "Content-Type: text/plain\n"

import cgi,sys

print "request is arriving to server"

payload = sys.stdin.read() 
fin = open("/home/ubuntu/test/text.txt", 'wb')
fin.write(payload)
m = {'id':2, 'name':'ranjeet'}
n = json.dumps(m)
o = json.loads(n)
print o['id']
#data= cgi.FieldStorage()
#x = data.getvalue("_tableName")
#print x

#print str(payload) + "hhhh"
