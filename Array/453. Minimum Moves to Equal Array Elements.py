class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini=min(nums)
        moves=0
        for i in nums:
            moves+=i-mini

        return moves