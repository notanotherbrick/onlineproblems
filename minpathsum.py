class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return
        opt = [0 for _ in xrange(len(grid[0]))]
        
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if j == 0: # first row or first column
                    opt[j] = opt[j] + grid[i][j]
                elif i == 0:
                    opt[j] = opt[j-1] + grid[i][j]

                else:
                    #print i, opt, opt[j] , opt[j-1]
                    opt[j] = min (opt[j-1],opt[j]) + grid [i][j]
        # return last element
            print opt
        return opt[-1]




S = Solution()
print S.minPathSum([[1,2,3,4],[6,1,7,8],[8,2,19,2],[19,8,1,6]])
