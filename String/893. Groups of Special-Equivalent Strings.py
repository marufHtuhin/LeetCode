class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res=set()
        for i in words:
            even=""
            odd=""
            for j in range(len(i)):
                if j%2==0:
                    even+=i[j]
                else:
                    odd+=i[j]
            even="".join(sorted(even))
            odd="".join(sorted(odd))
            res.add(str(even)+str(odd))

        return len(res)