class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len,reverse=True)
        res=""
        for i in words:
            if i+"#" not in res:
                res+=i+"#"

        return len(res)