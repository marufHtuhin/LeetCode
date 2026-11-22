class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        s=sorted(nums)
        n=len(nums)
        mid=(n+1)//2
        l,r=mid-1,n-1
        for i in range(n):
            if i%2==0:
                nums[i]=s[l]
                l-=1
            else:
                nums[i]=s[r]
                r-=1
                