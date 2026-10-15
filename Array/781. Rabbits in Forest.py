from collections import Counter
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        c=Counter(answers)
        s=0
        for i,j in c.items():
            s+=((i+j)//(i+1)*(i+1))

        return s