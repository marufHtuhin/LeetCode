from collections import Counter
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        c=Counter(s)
        res=[None]*len(s)
        i,n=0,len(s)
        for j in sorted(c,key=c.get,reverse=True):
            if c[j]>n//2+(n%2):
                return ""
            for k in range(c[j]):
                if i>=n:
                    i=1
                res[i]=j
                i+=2
        return "".join(res)