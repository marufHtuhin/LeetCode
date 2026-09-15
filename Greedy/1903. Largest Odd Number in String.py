class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        l=len(num)-1
        for i in range(l,-1,-1):
            c=num[i]
            if int(c)%2!=0:
                return num[:i+1]

        return ""