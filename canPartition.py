# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 14:01:00 2016

@author: Hobbiton
"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        s = sum(nums)
        #print s
        
        if s % 2 == 1:
            return False
            
        dp = [False] *(s/2 + 1)
        #print dp
        #nums.sort()
        
        dp[0] = True         
        
        for i in xrange(len(nums)):
            print dp
            for tot in xrange((s/2), -1, -1):
                #print 'dp is',  dp 
                if tot - nums[i] >= 0:
                    print tot, tot - nums[i]
                    dp[tot] = dp[tot] or dp[tot-nums[i]]
        
        print dp
        return dp[-1]
        
    def hashSol(self,nums):
            
            s = sum(nums)
            if s % 2 == 1:
                return False
            
            s = s/2
            seen = set([nums[0]])
            
            for n in nums[1:]:

                seen.update([n + v for v in seen])
                if s in seen:
                    return True
            #print seen
            return False

S=Solution()
print S.hashSol([1,5,11,5])