#!/usr/bin/python
import socket
import time

socket.setdefaulttimeout(3)
s = socket.socket()
target = "attackdirect.samsclass.info"
port = 80
s.connect((target, port))
s.send("GET / HTTP/1.1\nHost: " + target + "\n\n")
print(s.recv(1024))
s.close()

