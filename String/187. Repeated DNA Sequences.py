class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        c,res={},[]
        for i in range(len(s)-9):
            j=s[i:i+10]
            c[j]=c.get(j,0)+1
            if c[j]==2:
                res.append(j)
            
        return res