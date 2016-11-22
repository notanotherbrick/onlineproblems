# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 19:34:52 2016

@author: Gondor
"""

A=[0,1,2,3,4,5,6,7,8,9,10]
#n=len(A)

def recurr(B):
    n=len(B)
    if n==0:
        return[]
    elif n==1:
         return [B[0]]   
    temp=[]
#    print "here"
    for i in range(n):j:

#        print "hi"
        #print i
        t=recurr(A[0:i]+A[i+1:n])
        print t
        temp+=map(lambda x:x+A[i],t)
        #print i,temp
    return temp
    

recurr(A[:3])

import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
#MESSAGE = "Hello, World!"

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))

sock.recvfrom(1024)