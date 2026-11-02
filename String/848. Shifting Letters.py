class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        s = list(s)
        total = 0
        for i in range(len(s)-1,-1,-1):
            total+=shifts[i]
            s[i]=chr((ord(s[i])-ord('a')+total)%26+ord('a'))

        return ''.join(s)