class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=str(n)
        l=len(s)
        for i in range(l-1):
            if s[i]>s[i+1]:
                break
        else:
            return int(s)
        while i>0 and s[i]==s[i-1]:
            i-=1

        return int(str(int(s[:i+1])-1)+'9'*(l-i-1))