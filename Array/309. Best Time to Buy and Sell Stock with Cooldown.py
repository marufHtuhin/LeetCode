class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy,sell,hold=999999,0,0
        for i in prices:
            buy=min(buy,i-hold)
            hold=sell
            sell=max(sell,i-buy)
        return sell