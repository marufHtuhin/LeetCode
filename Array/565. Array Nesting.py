class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visi=[False]*len(nums)
        maxi=0
        for i in range(len(nums)):
            if visi[i]:
                continue
            l=0
            j=i
            while not visi[j]:
                visi[j]=True
                j=nums[j]
                l+=1
            maxi=max(maxi,l)
        return maxi