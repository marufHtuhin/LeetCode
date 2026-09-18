class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=str(num)
        maxi=s
        for i in s:
            if i!='9':
                maxi=s.replace(i,'9')
                break
        mini=s
        for i in s:
            if i!='0':
                mini=s.replace(i,'0')
                break

        return int(maxi)-int(mini)