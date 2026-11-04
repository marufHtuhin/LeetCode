class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        i,j=0,0
        for k in s:
            if k=='(':
                i+=1
            elif i:
                i-=1
            else:
                j+=1
                
        return i+j