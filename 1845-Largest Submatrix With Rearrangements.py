class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = 0

        for row in range(n):
            for col in range(m):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]
                    
            curr_row = sorted(matrix[row], reverse=True)
            
            for i in range(m):
                res = max(res, curr_row[i] * (i + 1))

        
        return res