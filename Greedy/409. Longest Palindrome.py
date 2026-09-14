from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=Counter(s)
        odd=0
        for i in c.values():
            if i%2==1:
                odd+=1
        if odd>1:
            return len(s)-odd+1
        return len(s)