class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[""]
        for i in s:
            if i.isdigit():
                res=[j+i for j in res]
            else:
                x=[j+i.lower() for j in res]
                y=[j+i.upper() for j in res]
                res=x+y

        return res