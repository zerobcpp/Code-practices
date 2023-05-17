# 1572. Matrix Diagonal Sum

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
    
    def diagonalSum(self, mat):
        res = 0
        n = len(mat)
        for i in range(n):
            res += mat[i][i]
            res += mat[i][n-i-1]
        
        if n % 2 == 1:
            res -= mat[n//2][n//2]
        
        return res