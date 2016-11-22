# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 13:54:57 2016

@author: Hobbiton
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.n=n
        return self.helper(range(1,n+1),k)
    
    def helper(self,L,k):
        if k==1:
            return [[i] for i in L]
        if k==self.n:
            return L

        return [[L[i]]+res
            for i in range(len(L))            
            for res in self.helper(L[:i]+L[i+1:],k-1)]        
    
            
        
       
S=Solution()       
print S.combine(4,3)