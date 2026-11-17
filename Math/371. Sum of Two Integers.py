class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask=0xFFFFFFFF
        while b:
            carry=(a&b)<<1
            a=(a^b)&mask
            b=carry&mask
        if a>0x7FFFFFFF:
            a=~(a^mask)

        return a