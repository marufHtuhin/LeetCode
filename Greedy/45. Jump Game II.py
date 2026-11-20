class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res,end,flag=0,0,0
        for i in range(len(nums)-1):
            flag=max(flag,i+nums[i])
            if flag>=len(nums)-1:
                res+=1
                break
            if i==end:
                res+=1
                end=flag

        return res