# -*- coding: utf-8 -*-
"""
Created on Sun Oct 09 14:17:39 2016

@author: Hobbiton
"""



def roman2int(s):
    #num=0
    if not s:
        return 0
    if s[0]=='L':
        return 50
    

    elif s[0:2]=='XL':
        print "here"
        return 40+roman2int(s[2:])    
    elif s[0]=='X':
        return 10+roman2int(s[1:])
    

          

    elif s=='I':
        return 1
    elif s=='II':
        return 2
    elif s=='III':
        return 3
    elif s=='IV':
        return 4
    elif s=='V':
        return 5
    elif s=='IX':
        return 9
    elif s[0]=='V':
        return 5+roman2int(s[1:])
    
print roman2int('XXVII')
print roman2int('XXVIII')
