class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        s,res=[0]*n,0
        for i in range(2,n):
            if s[i]:
                continue
            res+=1
            s[i*i:n:i]=[1]*((n-1)//i-i+1)
        return res