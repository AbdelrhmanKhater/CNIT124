#!/usr/bin/python
import socket

socket.setdefaulttimeout(3)
s = socket.socket()
target = raw_input("target:")
port = int(raw_input("port:"))
s.connect((target, port))
s.send("HEAD / HTTP/1.1\nHost: " + target + "\n\n")
print(s.recv(1024))
s.close()

