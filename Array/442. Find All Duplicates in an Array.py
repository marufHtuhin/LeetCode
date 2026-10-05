class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        l=(len(nums)+1)*[0]
        for i in nums:
            l[i]+=1
        for i in nums:
            if l[i]==2:
                res.append(i)
            l[i]-=1
        return res