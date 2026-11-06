class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        res=[]
        while a>0 or b>0:
            if len(res)>=2 and res[-1]==res[-2]:
                i=res[-1]=='b'
            else:
                i=a>=b
            
            if i:
                res.append('a')
                a-=1
            else:
                res.append('b')
                b-=1

        return "".join(res)