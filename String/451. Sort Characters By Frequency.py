class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq=Counter(s)
        chars=freq.most_common()
        res=[]
        for i,j in chars:
            res.append(i*j)

        return "".join(res)