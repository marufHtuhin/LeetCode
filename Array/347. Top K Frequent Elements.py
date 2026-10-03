class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        s={}
        for i in nums:
            if i in s:
                s[i]=s[i]+1
            else:
                s[i]=1
                
        arr=sorted(s,key=s.get,reverse=True)
        return (arr[:k])