from collections import Counter
class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        c=Counter()
        for i in words2:
            curr=Counter(i)
            for j in curr:
                c[j]=max(c[j],curr[j])
        res=[]
        for i in words1:
            curr=Counter(i)
            if all(curr[j]>=c[j] for j in c):
                res.append(i)
        
        return res