class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        m1=m2=101
        for i in prices:
            if i<=m1:
                m2=m1
                m1=i
            else:
                m2=min(m2,i)
        if m1+m2<=money:
            return money-(m1+m2)
        
        return money