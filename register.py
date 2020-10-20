# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:42:47 2020

@author: Anna Galsanova
"""

from urllib.parse import urlparse
import socket 

array = []
f = open('register.txt', encoding='utf-8')
lines = f.readlines()
for i in range(1, len(lines)):
    first = lines[i].strip().split(';')
    array.extend(first)
    
url = input("Input URL: ")
if 'www' in url:
    a = 1
else:
    a = 0
    
parse = urlparse(url)
domain = parse.netloc.split(".")[a:]
host = ".".join(domain)
print("Your domain: ", host)

if url in array:
    print ("Your url is blocked")
else:
    print("Your url is not blocked")

if host in array:
    print ("Index of your domain is blocked")
else:
    print("Your domain is not blocked")

ind = array.index(host)

ip = array[ind+1].strip().split(',')

print("IPs in the list: ", ip)

inip = socket.gethostbyname(host)
print("IP of your domain: ", myip)

if myip in array:
    eip = ip.index(inip)
    print("index of IP in array:", eip)
else:
    print("Your IP is not blocked")