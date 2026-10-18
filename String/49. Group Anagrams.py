class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        s={}
        for i in strs:
            new=''.join(sorted(i))
            if new not in s:
                s[new]=[]
            s[new].append(i)
        
        return list(s.values())