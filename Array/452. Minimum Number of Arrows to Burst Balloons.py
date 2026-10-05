class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:x[1])
        res,arrow=0,0
        for i,j in points:
            if res==0 or i>arrow:
                res,arrow=res+1,j
        
        return res