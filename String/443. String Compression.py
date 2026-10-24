class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n=len(chars)
        i,j=0,0
        while j<n:
            ch=chars[j]
            c=0
            while j<n and chars[j]==ch:
                c+=1
                j+=1
            if c==1:
                chars[i]=ch
                i+=1
            else:
                chars[i]=ch
                i+=1
                for k in str(c):
                    chars[i]=k
                    i+=1
        chars[:]=chars[:i]
        return i