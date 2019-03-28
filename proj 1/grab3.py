#!/usr/bin/python
import socket

socket.setdefaulttimeout(1)
s = socket.socket()
target = raw_input("target:")
port = int(raw_input("port:"))
s.connect((target, port))
print(s.recv(1024))
s.close()

