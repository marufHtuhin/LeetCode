class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        st=[]
        for i in num:
            while k>0 and st and st[-1]>i:
                st.pop()
                k-=1
            st.append(i)
        while st and k>0:
            st.pop()
            k-=1
        if not st:
            return "0"
            
        return str(int("".join(st)))