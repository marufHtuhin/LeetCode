class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for i in range(len(nums)):
            if i%2:
                res-=nums[i]
            else:
                res+=nums[i]
        return res