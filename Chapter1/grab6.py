import socket
import time
 
socket.setdefaulttimeout(1)
i = 3000
def conFunc(target, port):
    soc = socket.socket()
    soc.connect((target, port))
    soc.close()
def grab(target, port):
    soc = socket.socket()
    soc.connect((target, port))
    soc.send("HEAD / HTTP/1.1\nHost: " + target + "\n\n")
    print(soc.recv(1024))
    soc.close()
target = 'attackdirect.samsclass.info'
#s.connect((target,3100))
#conFunc(target, 3100)
#print('Connected to port: 3100')
while i<4000:
     try:
         conFunc(target, 3100)
         conFunc(target, i)
         time.sleep(2)
         grab(target, 3003)
         i=4000
     except Exception as e:
         #print(e)
         #print('Port',i,'does not work')
         i=i+100
         

