class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        l=len(colors)
        maxi=0
        for i in range(l-1,-1,-1):
            if colors[i]!=colors[0]:
                maxi=i
                break
        for i in range(l):
            if colors[i]!=colors[l-1]:
                maxi=max(maxi,l-i-1)
                break

        return maxi