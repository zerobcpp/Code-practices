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
            
            for i in range(right-1, left-1, -1):
                res.append(matrix[down][i])
            
            for i in range(down-1, up, -1):
                res.append(matrix[i][left])
                
            up += 1
            left += 1
            down -= 1
            right -= 1
            print(res)
        
        return res
                