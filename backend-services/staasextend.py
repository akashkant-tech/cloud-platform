#!/usr/bin/python36

import cgi
print("content-type: text/html")
print("\n")

import subprocess as sp

#print("<form>")
#print("Enter storage name <input type='text' name='sn'> ")
#print("Enter extended size in MB <input type='text' name='ss'> ")
#print("<input type='submit' value='submit'>")
#print("</form>")

form = cgi.FieldStorage()
stname = form.getvalue('sn')
stsize = form.getvalue('ss')

extend = sp.getstatusoutput("sudo ansible-playbook /root/lvresize.yml --extra-vars='x={0} y={1}'".format(stname,stsize))

if extend[0]==0:
        print("<h3>Storage extended successfully</h3>")
else:
      pass


