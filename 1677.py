class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    res += mat[i][j]
                elif i == (n-1) - j:
                    #print(i, j)
                    res += mat[i][j]
        
        return res