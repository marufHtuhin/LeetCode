class Solution(object):
    def canTransform(self, start, result):
        """
        :type start: str
        :type result: str
        :rtype: bool
        """
        if start.count('X')!=result.count('X'): 
            return False
        i,j,n=0,0,len(start)
        while i<n and j<n: 
            if start[i]=='X': 
                i+=1
                continue
            if result[j]=='X':
                j+=1
                continue
            if start[i]!=result[j]:
                return False
            if start[i]=='L' and i<j:
                return False
            if start[i]=='R' and i>j:
                return False
            i+=1
            j+=1
        return True