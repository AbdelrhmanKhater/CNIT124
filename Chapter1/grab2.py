#!/usr/bin/python
import socket

socket.setdefaulttimeout(1)
s = socket.socket()
target = "attackdirect.samsclass.info"
port = 22
port = int(port)
s.connect((target, port))
print(s.recv(1024))
s.close()

