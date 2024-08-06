class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        res = []
        up, down = 0, n - 1
        left, right = 0, m - 1
        while len(res) < n * m:
            
            for i in range(left, right+1):
                res.append(matrix[up][i])
            
            for i in range(up+1, down+1):
                res.append(matrix[i][right])
            if up != down:
                for i in range(right-1, left-1, -1):
                    res.append(matrix[down][i])
            if left != right:
                for i in range(down-1, up, -1):
                    res.append(matrix[i][left])

            up += 1
            left += 1
            down -= 1
            right -= 1
        #print(res)
        
        return res
    
    def spiralOrder(self, mat):
        n = len(mat)
        m = len(mat[0])
        res = []
        dirs = 1
        r, c = 0, -1
        while n * m > 0:
            for i in range(m):
                c += dirs
                res.append(mat[r][c])
                
            n -= 1
            
            #print(res, r, c)
            for i in range(n):
                r += dirs
                res.append(mat[r][c])
                
            m -= 1
            dirs *= -1
            
        
        return res