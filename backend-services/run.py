#!/usr/bin/python36

import cgi
print("content-type: text/html")
print("\n")

import subprocess as sp

form = cgi.FieldStorage()
cid = form.getvalue('cid')


stat=sp.getstatusoutput("sudo ssh 192.168.43.110  docker start " + cid)

print("<meta http-equiv=\"refresh\" content=\"0;url=http://192.168.43.185/cgi-bin/dockerlistv2.py\"/>\n")



