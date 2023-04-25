# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        l, r = 0, n * m - 1
        
        while l <= r:
            mid = l + (r-l) // 2
            i = mid // m
            j = mid % m
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False