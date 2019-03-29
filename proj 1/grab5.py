#!/usr/bin/python
import socket
import time

socket.setdefaulttimeout(3)
s = []
for i in range(0,3):
   s.append(socket.socket())
target = raw_input("target:")
for i in range(3100, 4000, 100):
   try:
      s[0].connect((target, 3100))
      s[1].connect((target, i))
      time.sleep(2)
      s[2].connect((target, 3003))
      s[2].send("HEAD / HTTP/1.1\nHost: " + target + "\n\n")
      print(s[2].recv(2048))
      print("HI")
      break
   except:
      print(i, "doesn't work")


