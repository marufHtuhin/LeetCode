class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=str(x)
        if s[0]=='-':
            rev='-'+s[:0:-1]
        else:
            rev=s[::-1]
        
        if -2**31<=int(rev)<=2**31-1:
            return int(rev)
        return 0