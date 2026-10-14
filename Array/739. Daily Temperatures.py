class Solution(object):
    def dailyTemperatures(self, temp):
        """
        :type temp=temperatures: List[int]
        :rtype: List[int]
        """
        s=[]
        res=[0]*len(temp)
        for i in range(len(temp)):
            while s and temp[i]>temp[s[-1]]:
                prev=s.pop()
                res[prev]=i-prev
            s.append(i)

        return res