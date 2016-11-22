# -*- coding: utf-8 -*-
"""
Created on Wed Oct 05 08:53:25 2016

@author: Hobbiton
"""



def fib(n):
    if n<1:
        print "N can't be less than one"
        return
    
    if n==1:
        res=0
    elif n==2:
        res=1
    else:
        f_n_1=1
        f_n_2=0
        for _ in xrange(3,n+1):
            f_n=f_n_1+f_n_2
            f_n_2=f_n_1
            f_n_1=f_n
        
        res=f_n
    
    if res%15==0:
        print "FizzBuzz"
        return res
    
    if res%5==0:
        print "Buzz"
        return res
    
    if res%3==0:
        print "Fizz"
        return res
    
    import math
    for divisor in xrange(2,int(math.sqrt(res))+1):
        if res%divisor==0: # F(n) not prime
            print res
            return res
            
    print "BuzzFizz"
    return res
    
