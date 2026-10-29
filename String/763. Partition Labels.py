class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res=[]
        seen={}
        maxi,c=0,0
        for i,j in enumerate(s):
            seen[j]=i
        for i,j in enumerate(s):
            maxi=max(maxi,seen[j])
            c+=1
            if i==maxi:
                res.append(c)
                c=0

        return res