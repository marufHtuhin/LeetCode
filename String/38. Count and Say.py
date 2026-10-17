class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s="1"
        for i in range(2,n+1):
            res=[]
            j=0
            while j<len(s):
                k=j
                while k<len(s) and s[k]==s[j]:
                    k+=1
                res.append(str(k-j))
                res.append(s[j])
                j=k
            s="".join(res)
        return s