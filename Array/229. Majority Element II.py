from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c=Counter(nums)
        l=len(nums)
        ans=[]
        for i,j in c.items():
            if j>l//3:
                ans.append(i)

        return ans