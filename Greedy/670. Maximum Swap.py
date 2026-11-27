class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums=list(str(num))
        last={int(j): i for i,j in enumerate(nums)}
        for i,j in enumerate(nums):
            for k in range(9,int(j),-1):
                if last.get(k,-1)>i:
                    nums[i],nums[last[k]]=nums[last[k]],nums[i]
                    return int(''.join(nums))

        return num