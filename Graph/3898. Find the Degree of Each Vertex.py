class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(matrix)):
            res.append(sum(matrix[i]))

        return res