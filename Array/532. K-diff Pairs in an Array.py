from collections import Counter
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<0:
            return 0
        c=Counter(nums)
        res=set([])
        for i in c.keys():
            if k==0:
                if c[i]>1:
                    res.add((i,i))
            else:
                j=i+k
                if j in c:
                    if i<=j:
                        res.add((i,j))
                    else:
                        res.add((j,i))

        return len(res)