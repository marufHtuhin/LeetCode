class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        c={i:0 for i in order}
        for i in s:
            if i in c:
                c[i]+=1
        sort=''
        for i in order:
            sort+=i*c[i]
        for i in s:
            if i not in order:
                sort+=i
        
        return sort