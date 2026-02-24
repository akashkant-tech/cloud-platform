#!/usr/bin/python36

import cgi
print("content-type: text/html")
print("\n")

import subprocess as sp

form = cgi.FieldStorage()
datanode = form.getvalue('dn')

if datanode == "one":
    dn1 = sp.getstatusoutput("sudo ansible-playbook /root/dn.yml")
    if dn1[0]==0:
       print("<h2>One data node setup successfully</h2>")
elif datanode == "two":
    dn2 = sp.getstatusotuput("sudo ansible-playbook /root/dn2.yml")
    if dn2[0] ==0:
       print("<h2>Tow data node setup successfully</h2>")
else:
    dn3 = sp.getstatusoutput("sudo ansible-playbook /root/dn3.yml")
    if dn3[0] ==0:
       print("<h2>Three data node setup successfully</h2>")


