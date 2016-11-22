# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 21:11:33 2016

@author: Hobbiton
"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        
        def gBST(l):
#            print l,type(l)
            """
            l : list[int]
            rtype : List[TreeNode]
            """
            
            if not l:
                return []
            if len(l)==1:
                return [TreeNode(l[0])]
            
            res=[]
            for i in xrange(len(l)):
                for x in gBST(l[:i]):
                    for r in gBST(l[i+1:]):
                        t=TreeNode(l[i])
                        t.left=x
                        t.right=r
                        res.append(t)
            
            return res or [None]
            
        return gBST(range(1,n+1))
        

print Solution().generateTrees(4)