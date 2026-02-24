#!/usr/bin/python36

import cgi
print("content-type: text/html")
print("\n")

import subprocess as sp

form = cgi.FieldStorage()
task = form.getvalue('tt')

if task == "one":
    dn1 = sp.getstatusoutput("sudo ansible-playbook /root/tt.yml")
    if dn1[0]==0:
       print("<h2>One task tracker setup successfully</h2>")
elif task == "two":
    dn2 = sp.getstatusotuput("sudo ansible-playbook /root/tt2.yml")
    if dn2[0] ==0:
       print("<h2>Two task tracker setup successfully</h2>")


