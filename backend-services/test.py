#!/usr/bin/python36

import cgi
print("content-type: text/html")
print("\n")

import subprocess as sp

form = cgi.FieldStorage()
cname = form.getvalue('cn')
#image = form.getvalue('img')

#cname = input("enter name")
container_name = sp.getstatusoutput("sudo ansible-playbook /root/shellinabox.yml --extra-vars='x={0}'".format(cname))

#print('<div style="padding:20px"><center><a href="http://192.168.43.110:9093" target="contframe">launch container</a><iframe name="contframe" height="300" width="800"></center></div>')

print("<meta http-equiv=\"refresh\" content=\"0;url=http://192.168.43.185/cgi-bin/dockerlistv2.py\"/>\n")

