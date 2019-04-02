#!/usr/bin/python
import socket
import time

socket.setdefaulttimeout(3)
s = socket.socket()
target = "attackdirect.samsclass.info"
port = 80
user = raw_input("username: ")
passwd = raw_input("pass: ")
l = len(user) + len(passwd) + 5
req = """POST /python/login1.php HTTP/1.1
Host: attackdirect.samsclass.info
Connection: keep-alive
Content-Length: """ + str(l) +\
"""
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: null
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Vary: Accept-Encoding
Content-Encoding: gzip
Accept-Language: en-US,en;q=0.9
Cookie: __cfduid=dbb1b428889c333626044aa2a8e4c59f51551031959
""" +\
"u=" + user + "&p=" + passwd
s.connect((target, port))
s.send(req)
print(s.recv(1024))
s.close()

