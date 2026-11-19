class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i,j,c=1,1,9
        while n>j*c:
            n-=j*c
            j+=1
            c*=10
            i*=10
        num=i+(n-1)//j
        
        return int(str(num)[(n-1)%j])