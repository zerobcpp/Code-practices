class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        N = len(mat)
        M = len(mat[0])
        row = [0] * N
        col = [0] * M
        
        for i in range(N):
            for j in range(M):
                if mat[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        #print(row, col)
        res = 0
        for i in range(N):
            for j in range(M):
                if row[i] == 1 and col[j] == 1 and mat[i][j] == 1:
                    #print(i, j)
                    res += 1
        
        return res
                    