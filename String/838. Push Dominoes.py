class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        s=list(dominoes)
        n=len(s)
        force=0
        for i in range(n):
            if s[i]=='R':
                force=n
            elif s[i]=='L':
                force=0
            else:
                force=max(force-1,0)
            s[i]=force
        force=0
        for i in range(n-1,-1,-1):
            if dominoes[i]=='L':
                force=n
            elif dominoes[i]=='R':
                force=0
            else:
                force=max(force-1,0)
            s[i]-=force
        return ''.join('R' if x>0 else 'L' if x<0 else '.' for x in s)