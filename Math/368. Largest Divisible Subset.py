class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s={-1:set()}
        for i in sorted(nums):
            best=set()
            for j in s:
                if j!=-1 and i%j==0:
                    if len(s[j])>len(best):
                        best=s[j]

            s[i]=best|{i}

        return list(max(s.values(),key=len))