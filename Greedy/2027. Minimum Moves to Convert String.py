class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        c,i=0,0
        while i<len(s):
            if s[i]=='O':
                i+=1
            else:
                c+=1
                i+=3
        return c