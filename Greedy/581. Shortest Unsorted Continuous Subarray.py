class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=sorted(nums)
        start,end,res=len(nums),0,0
        for i in range(len(nums)):
            if nums[i]!=s[i]:
                start=min(start,i)
                end=max(end,i)
                
        if end-start>=0:
            res=end-start+1
        else:
            return 0
        return res