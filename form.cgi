#! /usr/bin/env python 
# -*- coding: UTF8 -*- 
"""CGI form example 
""" 
import cgi 
import cgitb 
import time 
# Enable CGI traceback 
cgitb.enable() 
# Create datestamp 
now = time.strftime("%A %d %B %Y") 
# Get the contents of the form 
form = cgi.FieldStorage() 
name = form.getvalue('name', 'new user') 
def print_content(): 
    print("Content-type: text/html") 
    print() 
def print_header(): 
    print("""<html> 
     <head> 
     <title>Simple CGI form</title> 
     </head> 
     <body>""") 
def print_form(): 
     print(""" 
     <form action='form.cgi'> 
     nter your name: <input type='text' name='name' /> 
     <input type='submit' /> 
     </form> 
     """) 
def print_footer(): 
    print("</body></html>") 
print_content() 
print_header() 
print("""<h1>It's {0!s}!</h1> 
<p>Hello {1!s}, your server is correctly set up to run Python programs.</p>""".format(now,  
name)) 
print_form() 
print_footer()
