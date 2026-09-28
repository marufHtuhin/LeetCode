class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i,j,total=0,0,0
        res=999999
        while j<len(nums):
            total+=nums[j]
            while total>=target:
                res=min(res,j-i+1)
                total-=nums[i]
                i+=1
            j+=1
        if res==999999:
            return 0
        else:
            return res