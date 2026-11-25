class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        res,prev=0,float('-inf')
        for i in intervals:
            if i[0]>=prev:
                prev=i[1]
            else:
                res+=1
                prev=min(prev,i[1])

        return res