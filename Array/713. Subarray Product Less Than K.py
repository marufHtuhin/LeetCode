class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=len(nums)
        res,j,mul=0,0,1
        if k <= 1:
            return 0
        for i in range(l):
            mul*=nums[i]
            while mul>=k:
                mul//=nums[j]
                j+=1
            res+=i-j+1

        return res