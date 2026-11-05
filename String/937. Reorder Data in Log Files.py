class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        i=[]
        j=[]
        for k in logs:
            if k[-1].isdigit():
                i.append(k)
            else:
                j.append(k)
        j=sorted(j,key=lambda x:(x.split()[1:],x.split()[0]))
        return j+i