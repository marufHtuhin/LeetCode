from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq=defaultdict(int)
        i,res=0,0
        for j in range(len(s)):
            freq[s[j]]+=1
            maxi=max(freq.values())
            curr=j-i+1
            if curr-maxi>k:
                freq[s[i]]-=1
                i+=1
            res=max(res,j-i+1)

        return res