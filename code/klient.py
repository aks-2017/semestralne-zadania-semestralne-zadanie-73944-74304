#!/usr/bin/env python

import socket
import time

TCP_IP = '10.0.0.2'
TCP_PORT = 5001
TCP_PORT2 = 5002
BUFFER_SIZE = 2048
#MESSAGE = "Suspendisse potenti. Quisque aliquam eros id diam egestas pulvinar. $


#prvy soket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#for x in range(0, 10):
#    MESSAGE = "%f" % time.time()
#    s.send(MESSAGE)
#    time.sleep(1)

#druhy soket
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((TCP_IP, TCP_PORT2))
for x in range(0, 10):
    MESSAGE = "%f" % time.time()
    s.send(MESSAGE)
    s2.send(MESSAGE)
    time.sleep(1)

#data = s.recv(BUFFER_SIZE)
s.close()
s2.close()
