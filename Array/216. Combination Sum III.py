class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        curr,res=[],[]
        i,j=1,0
        q=[(i,curr,j)]
        while q:
            i,curr,j=q.pop()
            if j==n and len(curr)==k:
                res.append(curr)
            else:
                for x in range(i,10):
                    if j+x>n:
                        break
                    q.append((x+1,curr+[x],j+x))

        return res