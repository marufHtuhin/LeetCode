class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        curr,total,res=0,0,0
        for i in range(len(arr)):
            curr+=arr[i]
            total+=i
            if curr==total:
                res+=1

        return res