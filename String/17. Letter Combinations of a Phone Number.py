class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        val=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res=[""]
        for i in digits:
            letters=val[int(i)-2]
            temp=[]
            for j in res:
                for k in letters:
                    temp.append(j+k)
            res=temp
        return res