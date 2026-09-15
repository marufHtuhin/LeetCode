from heapq import heapify, heappop, heappush
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapify(nums)
        while nums[0]<0 and k:
            heappush(nums,-heappop(nums))
            k-=1
        if k%2:
            nums[0]=-nums[0]
        return sum(nums)