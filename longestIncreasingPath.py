# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 18:25:19 2016

@author: Hobbiton
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0 
            
        def helper(r,c) :
            if dp[r][c] != -1:
                return dp[r][c]
            if r < 0 or r > len(matrix) or c < 0 or c > len(matrix[0]):
                return 0
            
            moves = [(-1,0),(1,0),(0,1),(0,-1)]
            for m_r, m_c in moves:
                
        
        for m in moves:
            
        

S = Solution()
S.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])