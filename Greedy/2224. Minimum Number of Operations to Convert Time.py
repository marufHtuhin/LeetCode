class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        curr=60*int(current[0:2])+int(current[3:5])
        tar=60*int(correct[0:2])+int(correct[3:5])
        diff=tar-curr
        c=0
        for i in [60,15,5,1]:
            c+=diff//i
            diff%=i
        
        return c