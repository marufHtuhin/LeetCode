class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        w=[words[0]]
        g=[groups[0]]
        for i in range(1,len(groups)):
            if groups[i]!=g[-1]:
                w.append(words[i])
                g.append(groups[i])
        
        return w