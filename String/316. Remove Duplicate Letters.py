class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        seen=set()
        end={}
        for i in range(len(s)):
            end[s[i]]=i
        for i,j in enumerate(s):
            if j in seen:
                continue
            else:
                while st and st[-1]>j and end[st[-1]]>i:
                    rm=st.pop()
                    seen.remove(rm)
                seen.add(j)
                st.append(j)

        return ''.join(st)