class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        nums.sort()
        
        first = (len(nums) -1) / 2
        second = len(nums) - 1
        
        res = [-1]* len(nums)
        i = 0 
        #print nums
        while i < len(nums):
            if i % 2 == 0:
                #print i, first
                res[i] = nums[first]
                first -= 1
            else:
                res[i] = nums[second]
                second -= 1
            i+=1 
        print res
        
S=Solution()
S.wiggleSort([1,5,1,3,6,3])