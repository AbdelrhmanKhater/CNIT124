#!/usr/bin/python
import socket

socket.setdefaulttimeout(1)
s = socket.socket()
s.connect(("attackdirect.samsclass.info", 80))
print(s.recv(1024))
s.close()

