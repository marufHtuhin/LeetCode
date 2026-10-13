class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        s=set()
        res=""
        for i in words:
            if len(i)==1 or i[:-1] in s:
                s.add(i)
                if len(i)>len(res):
                    res=i
        return res