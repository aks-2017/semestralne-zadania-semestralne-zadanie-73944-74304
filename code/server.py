#!/usr/bin/env python

import socket
import time

TCP_IP = '10.0.0.2'
TCP_PORT = 5001
TCP_PORT2 = 5002
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.bind((TCP_IP, TCP_PORT2))
s2.listen(10)

conn, addr = s.accept()
conn2, addr = s2.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if len(data)> 0: kon1 = time.time()
    data2 =  conn2.recv(BUFFER_SIZE)
    if len(data)> 0: kon2 = time.time()
    if not data: break
    if not data2: break
    print "received data1: %s - %f" % (data, kon1)
    print "received data2: %s - %f" % (data2, kon2)
    #conn.send(data)  # echo
conn.close()
conn2.close()
#conn2, addr = s2.accept()
#print 'Connection address:', addr
#while 1:
#    data = conn2.recv(BUFFER_SIZE)
#    koniec = time.time()
#    cas = data[7:]
