class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res=[0]*n
        x,y=1,k+1
        for i in range(k+1):
            if i%2:
                res[i]=y
                y-=1
            else:
                res[i]=x
                x+=1
        for i in range(k+1,n):
            res[i]=i+1
        return res