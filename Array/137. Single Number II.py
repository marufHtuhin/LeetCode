class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    c+=1
            if c==1:
                return nums[i]
                break