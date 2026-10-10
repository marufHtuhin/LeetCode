class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        c=0
        for i in range(len(nums)-1,-1,-1):
            j=0
            k=i-1
            while j<k:
                if nums[j]+nums[k]>nums[i]:
                    c+=k-j
                    k-=1
                else:
                    j+=1
        return c