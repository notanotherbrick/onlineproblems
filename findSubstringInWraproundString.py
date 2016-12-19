# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 00:19:32 2016

@author: Hobbiton
"""

class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p:
            return 0
        dp=[0]*26
        continuous=0
        
        
        for i in xrange(len(p)):
            if i>0 and (ord(p[i])-ord(p[i-1])==1 or ord(p[i])-ord(p[i-1])==-25):
                continuous+=1
                #print i, 'here',continuous
            else:
                continuous=1
            dp[ord(p[i])-ord('a')]=max(dp[ord(p[i])-ord('a')],continuous)
        
        
        
            
        #print dp
        return sum(dp)

s=Solution()
print s.findSubstringInWraproundString('ab')