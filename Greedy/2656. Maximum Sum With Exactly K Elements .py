class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=nums[0]
        for i in nums:
            if i>n:
                n=i
        res=0
        for i in range(0,k):
            res+=n
            n+=1
        return res