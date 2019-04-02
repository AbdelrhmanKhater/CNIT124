#!/usr/bin/python
import socket

socket.setdefaulttimeout(3)
s = socket.socket()
target = raw_input("target:")
for i in range(1000, 65000, 1000):
    try:
       s.connect((target, i))
       s.send("ak7")
       print(s.recv(1024))
       s.close()
    except Exception:
       print(i, "doesn't work")

