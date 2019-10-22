#!usr/bin/env python
import cgi   #to receive data from web server common gateway interface 

print("Content-type:text/html") #to store only html code and output of html
print("")# to ignore other details which we get from web server

web_data=cgi.FieldStorage()# store complete data of html page

#extracting variables from html page
x=web_data.getvalue('n1')
print(type(x))  #to get to know the type of values receiving
y=web_data.getvalue('n2')
print(type(y))  #to get to know the type of values receiving

print(x+y)
