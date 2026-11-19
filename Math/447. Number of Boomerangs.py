class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans=0
        for i,j in points:
            c={}

            for m,k in points:
                d=(m-i)**2 +(k-j)**2
                if d in c:
                    ans+=2*c[d]
                    c[d]+=1
                else:
                    c[d]=1

        return ans