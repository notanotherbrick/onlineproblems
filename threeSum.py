class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in xrange(len(nums)):

        	if i > 0 and nums[i] == nums[i-1]:
        		continue
        	#print seen_i, nums[i] in seen_i
        	while l < r
	        	l = i+1
	        	r = len(nums) - 1
	        	s = nums[i] + nums[l] + nums[r]

	        	if s > 0:
	        		r -= 1
	        	elif s < 0:
	        		l += 1
	        	else:
	        		res.append([nums[i],nums[l],nums[r]])



        return res



S = Solution()
print S.threeSum([0,0,0,0,0])