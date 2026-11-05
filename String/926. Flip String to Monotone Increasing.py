class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        i,j=0,0
        for k in s:
            if k=='0':
                i+=1
        res=i
        for k in s:
            if k=='0':
                i-=1
            elif k=='1':
                j+=1
            res=min(res,i+j)
        
        return res