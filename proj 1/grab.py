#!/usr/bin/python
import socket


s = socket.socket()
s.connect(("attackdirect.samsclass.info", 22))
print(s.recv(1024))
s.close()

