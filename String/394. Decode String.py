class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        num,temp=0,""
        for i in s:
            if i.isdigit():
                num=(num*10)+int(i)
            elif i=='[':
                st.append((temp,num))
                num=0
                temp=""
            elif i==']':
                string,nums=st.pop()
                temp=string+(temp*nums)
            else:
                temp+=i

        return temp