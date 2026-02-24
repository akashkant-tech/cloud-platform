#!/usr/bin/python36

import cgi
print("content-type: text/html")
print("\n")

import subprocess as sp

#form = cgi.FieldStorage()
#language = form.getvalue('lang')
#print("<a href='http://192.168.43.110:9093' target='cframe'>Click here</a>")
#print("<iframe name='cframe' width='100%' height='25%'>container console</iframe>")

#dlist=sp.getoutput("sudo ssh 192.168.43.110 docker ps -a | sudo grep -E 'Up|Created'")
dlist=sp.getoutput("sudo ssh 192.168.43.110 docker ps -a | sudo grep -E 'Up|Created|Exited'")
#print(dlist)

d2list=dlist.split("\n")

#d3list=d2list.split(",")

#print(d2list)
print("""
<CTYPE html>
<html>
<head>
<style>
table, th, td {
    border: 1px solid black;
}
</style>
</head>
<body>

<h2>Docker os list</h2>
<p>Click on 'start' to use the os or 'stop' to stop the running os.</p>
""")
print("<table style='width:100%'>")
print("<tr>")
print("<th>Container ID</th>")
print("<th>Image</th>") 
print("<th>Command</th>")
print("<th>Status</th>")
print("<th>Name</th>")
print("<th>Start</th>")
print("<th>Stop</th>")
print("</tr>")

a=0
#f=open("doclist.txt","a+")
for i in d2list[0:] :
	print("<tr>")
	j = i.split()
	a=a+1
	print(a)
	#f.write(str(a)+":"+j[0]+"\n")
	cid=str(j[0])
	print("<td>"+j[0]+"</td>")
	print("<td>"+j[1]+"</td>")
	print("<td>"+j[2]+"</td>")
	print("<td>"+j[6]+"</td>")
	print("<td>"+j[-1]+"</td>")
	print("<form  action='run.py'>")
	print("<td><input type='hidden' name='cid' value='"+cid+"'><input type='submit' value='Run'></td>")
	print("</form>")
	print("<form  action='kill.py'>")
	print("<td><input type='hidden' name='cid' value='"+cid+"'><input type='submit' value='Kill'></td>")
	print("</form>")
	print("</tr>")
#f.close()
print("<a href='http://192.168.43.110:9093' target='cframe'>START</a>")
print("<iframe name='cframe' width='100%' height='55%'>container console</iframe>")

