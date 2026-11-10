class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        x=min(m-1,n-1)
        res=1
        for i in range(1,x+1):
            res=res*(m+n-2-x+i)//i

        return res