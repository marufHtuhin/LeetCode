class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        s=[]
        for i,j in enumerate(board):
            for k,l in enumerate(j):
                if l!='.':
                    s+=[(l,k),(i,l),(i/3,k/3,l)]

        return len(s)==len(set(s))