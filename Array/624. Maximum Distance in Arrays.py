class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        res=0
        mini,maxi=arrays[0][0],arrays[0][-1]
        for i in arrays[1:]:
            res=max(res,i[-1]-mini,maxi-i[0])
            mini=min(mini,i[0])
            maxi=max(maxi,i[-1])

        return res