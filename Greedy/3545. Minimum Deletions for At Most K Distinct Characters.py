class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        x=sorted(d.values())
        l=len(x)-k
        res=0
        for i in range(l):
            res+=x[i]
        return res