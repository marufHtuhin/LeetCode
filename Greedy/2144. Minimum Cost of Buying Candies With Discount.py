class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)
        res=0
        for i in range(len(cost)):
            if i%3!=2:
                res+=cost[i]

        return res