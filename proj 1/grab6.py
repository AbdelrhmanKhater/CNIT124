import socket
import time
 
socket.setdefaulttimeout(1)
s = socket.socket()
a = socket.socket()
p = socket.socket()
i = 3000
def conFunc(target, port):
    soc = socket.socket()
    soc.connect((target, port))
    soc.close()
def grab(target, port):
    soc = socket.socket()
    soc.connect((target, port))
    soc.send("HEAD / HTTP/1.1\nHost: " + target + "\n\n")
    soc.recv(1024)
    soc.close()
target = 'attackdirect.samsclass.info'
#s.connect((target,3100))
conFunc(target, 3100)
print('Connected to port: 3100')
while i<4000:
     try:
         #a.connect((target,i))

         conFunc(target, i)
         #print('Connected to 2nd port')
         #print('Knocking...')
         time.sleep(2)
         #p.connect((target,3003))
         #p.send('HEAD / HTTP/1.1\nHost: '+ target +'\n\n')
         #print(p.recv(1024))
         grab(target, 3003)
         i=4000
     except Exception as e:
         #print(e)
         #print('Port',i,'does not work')
         i=i+100
     finally:
         pass
         #s.close()
         #a.close()
         #p.close()

a.close()
s.close()
p.close()

