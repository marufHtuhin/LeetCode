class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=[1,2,2]
        i=2
        while len(s)<n:
            s+=[3-s[-1]]*s[i]
            i+=1

        return s[:n].count(1)