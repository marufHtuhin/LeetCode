class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m={0:-1}
        c,res=0,0
        for i,j in enumerate(nums):
            c+=1 if j==1 else -1
            if c in m:
                res=max(res,i-m[c])
            else:
                m[c]=i

        return res