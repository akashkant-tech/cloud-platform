#!/usr/bin/python36

import cgi
print("content-type: text/html")
print("\n")

import subprocess as sp

form = cgi.FieldStorage()
language = form.getvalue('lang')

if language == "Python3":
      print("<a href='http://192.168.43.110:1113' target='f1'>Click here</a>")
      print("<iframe name='f1' height='300' width='800'></iframe>")
      print("<h3>Enter your Username and password to continue</h3>")
elif language == "Python2":
      print("<a href='http://192.168.43.110:1113' target='f1'>Click here</a>")
      print("<iframe name='f1' height='300' width='800'></iframe>")
      print("<h3>Enter your Username and password to continue</h3>")

elif language == "Ruby":
      print("<a href='http://192.168.43.110:1113' target='f1'>Click here</a>")
      print("<iframe name='f1' height='300' width='800'></iframe>")
      print("<h3>Enter your Username and password to continue</h3>")

elif language == "Perl":
      print("<a href='http://192.168.43.110:1113' target='f1'>Click here</a>")
      print("<iframe name='f1' height='300' width='800'></iframe>")
      print("<h3>Enter your Username and password to continue</h3>")

else:
      print("<a href='http://192.168.43.185/java.html' target='f1'>Click here</a>")
      print("<iframe name='f1' height='300' width='800'></iframe>")



