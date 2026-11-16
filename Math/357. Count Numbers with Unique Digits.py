class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        res=10
        curr=9
        for i in range(2,n+1):
            res+=curr*(11-i)
            curr*=11-i
        
        return res