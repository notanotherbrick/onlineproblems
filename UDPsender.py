# -*- coding: utf-8 -*-
"""
Created on Sat Dec 03 23:43:09 2016

@author: Hobbiton
"""

import socket
UDP_IP = "10.42.0.1"
UDP_PORT = 8888    

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT


sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
import datetime
from time import sleep

while(1):
    sleep(2)
    MESSAGE=str(datetime.datetime.now())
    print MESSAGE
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))