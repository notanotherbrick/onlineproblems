class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        
        res = 1
        
        for i in xrange(m-1,0,-1):
            print 'h',m-i, i + n -1
            res *= (i + n -1)
            res /= (m-i)
            print res
        return res

S = Solution()
print S.uniquePaths(1,1)
print S.uniquePaths(2,2)
print S.uniquePaths(3,4)
print S.uniquePaths(4,6)