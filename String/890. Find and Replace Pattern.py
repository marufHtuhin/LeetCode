class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res=[]
        for i in words:
            if len(set(i))==len(set(pattern))==len(set(zip(i,pattern))):
                res.append(i)

        return res