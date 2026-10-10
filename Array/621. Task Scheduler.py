class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq=Counter(tasks).values()
        maxi=max(freq)
        cnt=freq.count(maxi)
        res=(maxi-1)*(n+1)+cnt

        return max(res,len(tasks))