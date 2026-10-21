class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s=[set(i) for i in words]
        maxi=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not (s[i] & s[j]):
                    maxi=max(maxi,len(words[i])*len(words[j]))
                    
        return maxi