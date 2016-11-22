# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 13:40:57 2016

@author: Hobbiton
"""

class ringBuffer(object):
    def __init__(self,size=10):
        self.size=size
        self.array=[-1]*size
        self.latest=0
        self.oldest=0
    def insert_elem(self,ele):
#        if self.array[self.latest]==-1: #empty location
#            self.array[self.latest]=ele
#            self.latest=(self.latest+1)%10
#        
#        else:
#            self.array[self.latest]=ele
#            self.latest=(self.latest+1)%10
#            self.oldest=(self.oldest+1)%10
            self.array[self.latest]=ele
            self.latest=(self.latest+1)%self.size
            
    def get_elems(self):
        res=[]
        i=self.latest-1
        count=0
        while (self.array[self.latest]!=-1) and count < self.size:
            print count, self.array[i]            
            res.append(self.array[i])
            i-=1
            i%=self.size
            count+=1
        return res            
        
    def peak(self):
        print self.array
        
        
        
r=ringBuffer(4)
r.peak()
r.insert_elem(1)
r.insert_elem(2)
r.insert_elem(3)
r.peak()
r.insert_elem(4)
r.insert_elem(5)
r.insert_elem(6)
r.peak()
print r.get_elems()
r.insert_elem(7)
r.insert_elem(8)
r.insert_elem(9)
print r.get_elems()
r.peak()
r.insert_elem(11)
print r.get_elems()


