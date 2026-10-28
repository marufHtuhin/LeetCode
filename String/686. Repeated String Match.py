class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        n=len(b)//len(a)
        i=1
        while i<=n+2:
            if b in a*i:
                return i
            else:
                i+=1
        
        return -1