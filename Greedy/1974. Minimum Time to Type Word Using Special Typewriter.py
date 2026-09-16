class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        t=0
        curr='a'
        for i in word:
            diff=abs(ord(curr)-ord(i))
            t+=min(diff,26-diff)+1
            curr=i

        return t