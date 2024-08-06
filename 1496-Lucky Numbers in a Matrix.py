class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = []
        cols = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            mn = float('inf')
            for j in range(m):
                mn = min(mn, matrix[i][j])
            rows.append(mn)
        
        for i in range(m):
            mx = 0
            for j in range(n):
                mx = max(mx, matrix[j][i])
            cols.append(mx)
        
        res = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == rows[i] and matrix[i][j] == cols[j]:
                    res.append(matrix[i][j])
        
        return res
                
            