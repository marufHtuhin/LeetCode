class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        res=[False]*(len(s)+1)
        res[0]=True
        for i in range(len(s)):
            for j in range(i,len(s)):
                if res[i] and s[i:j+1] in wordDict:
                    res[j+1]=True

        return res[-1]