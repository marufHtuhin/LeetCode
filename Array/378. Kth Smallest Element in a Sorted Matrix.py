class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        arr=[]
        for i in matrix:
            arr.extend(i)
        arr.sort()
        return arr[k-1]