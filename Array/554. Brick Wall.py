class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edge={}
        maxi=0
        for i in range(len(wall)):
            pos=0
            for j in range(len(wall[i])-1):
                curr=wall[i][j]
                pos+=curr
                edge[pos]=edge.get(pos,0)+1
                maxi=max(edge[pos],maxi)

        return len(wall)-maxi