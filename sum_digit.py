# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:33:35 2016

@author: Hobbiton
"""

n = 37
res=0

for i in xrange(1,1+int(n*0.5)):
    if n%i==0:
        res=better(res,i)
        #print res,i

res=better(res,n)
print res
