class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        l=len(word)
        if l<=8:
            return l
        elif l<=16:
            return 8+2*(l-8)
        elif l<=24:
            return 24+3*(l-16)
        else:
            return 48+4*(l-24)