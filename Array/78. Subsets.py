class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        total=1<<n
        res=[]
        for i in range(total):
            s=[]
            for j in range(n):
                if i&(1<<j):
                    s.append(nums[j])
            res.append(s)
        
        return res