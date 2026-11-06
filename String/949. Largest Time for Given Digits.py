class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        arr.sort()
        for i in range(23,-1,-1):
            for j in range(59,-1,-1):
                t=[i//10,i%10,j//10,j%10]
                ts=sorted(t)
                if ts==arr:
                    return str(t[0])+str(t[1])+':'+str(t[2])+str(t[3])

        return ''