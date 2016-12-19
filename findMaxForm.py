# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 01:07:58 2016

@author: Hobbiton
"""

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int zeros
        :type n: int
        :rtype: int
        """
        
        dp=[[[-1]*len(strs) for _ in xrange(m)] for _ in xrange(n)]
        
        def helper(i,m,n):
            if i==len(strs):
                return 0
            if dp[i][m][n]!=-1:
                return dp[i][m][n]
            ones=strs[i].count('1')
            zeros=strs[i].count('0')
            if m<zeros or n < ones:
                dp[i][m][n]=dp[i+1][m][n]
            else:
                dp[i][m][n]=max(dp[i+1][m][n],1+dp[i+1][m-zeros][n-ones])
            return dp[i][m][n]
            
        
        return helper(0,m-1,n-1)
            
            
        
        
s=Solution()
print s.findMaxForm(["10","0001","111001","1","0"],5,3)