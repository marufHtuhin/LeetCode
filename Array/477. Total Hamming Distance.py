class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        res=0
        for i in range(30):
            c=0
            for j in nums:
                c+=(j>>i)&1
            res+=c*(l-c)
        return res