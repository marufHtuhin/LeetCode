class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        def sub(x):
            i=0
            for j in x:
                k=s.find(j,i)
                if k==-1:
                    return False
                i=k+1
            return True
            
        return sum(sub(i) for i in words)