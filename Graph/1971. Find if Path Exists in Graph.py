class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        neigh=defaultdict(list)
        for i,j in edges:
            neigh[i].append(j)
            neigh[j].append(i)
        q=deque([source])
        s=set([source])
        while q:
            node=q.popleft()
            if node==destination:
                return True
            for n in neigh[node]:
                if n not in s:
                    s.add(n)
                    q.append(n)

        return False