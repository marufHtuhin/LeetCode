class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = -1 if (dividend<0)!=(divisor<0) else 1
        x=abs(dividend)
        y=abs(divisor)
        res=0
        while x>=y:
            temp=y
            multiple=1
            while x>=(temp<<1):
                temp<<=1
                multiple<<=1
            x-=temp
            res+=multiple

        if sign==-1:
            res=-res
        return min(max(res,-2**31),2**31-1)