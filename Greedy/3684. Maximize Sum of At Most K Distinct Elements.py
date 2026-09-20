class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        s=list(set(nums))
        s.sort(reverse=True)

        return s[:k]