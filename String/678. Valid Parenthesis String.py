class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i,j=0,0
        for c in s:
            if c=='(':
                i+=1
                j+=1
            elif c==')':
                i-=1
                j-=1
            else:
                i-=1
                j+=1
            
            if j<0:
                return False
            i=max(i,0)
        return i==0