#!/usr/bin/python

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = raw_input("Target: ")
port = int(raw_input("Port: "))
if s.connect_ex((target, port)):
   print("Port " + str(port) + " is closed")
else:
   print("Port " + str(port) + " is open")
