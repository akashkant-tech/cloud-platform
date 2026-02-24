#!/usr/bin/python36

print("content-type: text/html")    
print("\n")
import subprocess as sp

print ("welcome to my tools")

#cmd = input("enter cmd : ")

form = cgi.FieldStorage()

data = form.getvalue('c')

print(data)
o = sp.getoutput(cmd)
print(o)

