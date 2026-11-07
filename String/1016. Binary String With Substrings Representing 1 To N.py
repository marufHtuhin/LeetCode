class Solution(object):
    def queryString(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: bool
        """
        if n>1000:
            n=1000
        for i in range(1,n+1):
            if bin(i)[2:] not in s:
                return False

        return True