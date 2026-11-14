class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        area1=(ax2-ax1)*(ay2-ay1)
        area2=(bx2-bx1)*(by2-by1)
        x1=max(ax1,bx1)
        y1=max(ay1,by1)
        x2=min(ax2,bx2)
        y2=min(ay2,by2) 
        inter=0
        if x1<x2 and y1<y2:
            inter=(x2-x1)*(y2-y1)
            
        return area1+area2-inter