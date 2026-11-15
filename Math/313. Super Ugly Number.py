class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res=[1]*n
        i=[0]*len(primes)
        val=primes[:]
        for j in range(1,n):
            m=min(val)
            res[j]=m
            for k,x in enumerate(primes):
                if val[k]==m:
                    i[k]+=1
                    val[k]=res[i[k]]*x

        return res[-1]