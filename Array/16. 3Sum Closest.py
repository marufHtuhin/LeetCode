class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i,n=0,len(nums)
        clst=nums[0]+nums[1]+nums[2]
        while i<n-2:
            j=n-1
            k=i+1
            while k<j:
                s=nums[i]+nums[j]+nums[k]
                if abs(s-target)<abs(clst-target):
                    clst=s
                if s==target:
                    return target
                elif s<target:
                    k+=1
                else:
                    j-=1
            i+=1
        return clst