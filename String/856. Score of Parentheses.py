class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        st=[0]
        for i in s:
            if i=='(':
                st.append(0)
            else:
                curr=st.pop()
                st[-1]+=max(1,2*curr)

        return st[0]