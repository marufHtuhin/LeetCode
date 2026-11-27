from collections import Counter
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c=Counter(nums)
        for i in sorted(c.keys()):
            while c[i]>0:
                end=0
                j=i
                k=0
                while c[j]>=end:
                    end=c[j]
                    c[j]-=1
                    j+=1
                    k+=1
                if k<3:
                    return False

        return True