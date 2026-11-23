class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i=j=float('inf')
        for k in nums:
            if k<=i:
                i=k
            elif k<=j:
                j=k
            else:
                return True

        return False