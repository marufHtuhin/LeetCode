class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=len(nums)*[-1]
        for i in range(len(nums)):
            j=(i+1)%len(nums)
            while i!=j:
                if nums[j]>nums[i]:
                    res[i]=nums[j]
                    break
                else:
                    j=(j+1)%len(nums)
        return res