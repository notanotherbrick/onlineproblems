# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 18:45:09 2016

@author: Hobbiton
"""

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        
        if IP.find(".")!=-1:
            IP=IP.split(".")
            if len(IP)!=4:
                return "Neither"
            for substr in IP:
                if not substr or len(substr)>3:
                    return "Neither"
                try:
                    c=int(substr)
                except ValueError:
                    return "Neither"
                
                #print c,len(substr)>1
                if substr[0]=='0' and (c!=0 or len(substr)>1) :
                        return "Neither"
                if c >255 or c < 0:
                        return "Neither"
            
            return "IPv4"
        
        elif IP.find(":")!=-1:
            IP=IP.split(":")
            if len(IP)!=8:
                return "Neither"
            for substr in IP:
                if not substr or len(substr)>4:
                    return "Neither"
                for q in substr:
                    c=ord(q)
                    if not (97 <= c <= 102 or 48 <= c <= 57 or 65 <= c <= 70):
                        return "Neither"
            
            return "IPv6"
                        
                    
        else:
            return "Neither"
            
    
s=Solution()
print s.validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
print s.validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334")
print s.validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334")
print s.validIPAddress("2001:0db8:85a3::8A2E:0370:7334")
print s.validIPAddress("172.16.254.01")
print s.validIPAddress("00.0.0.0")