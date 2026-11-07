class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<3:
            return False
        res=[]
        for i in s:
            res.append(i)
            if len(res)>=3:
                if res[-1]=='c' and res[-2]=='b' and res[-3]=='a':
                    res.pop()
                    res.pop()
                    res.pop()
                    
        return not res