class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy,sell=-prices[0],0
        for i in range(1,len(prices)):
            buy=max(buy,sell-prices[i])
            sell=max(sell,buy+prices[i]-fee)

        return sell