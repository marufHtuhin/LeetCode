class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        pref=[1]*l
        suff=[1]*l
        ans=[]
        for i in range(1,l):
            pref[i]=pref[i-1]*nums[i-1]
        for i in range(l-2,-1,-1):
            suff[i]=suff[i+1]*nums[i+1]
        for i in range(l):
            ans.append(pref[i]*suff[i])

        return ans