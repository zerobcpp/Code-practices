class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for i in range(n)]
        count = 1
        m = 3
        r, c = 0, -1
        direction = 1
        while n * m > 0:
            
            for i in range(m):
                c += direction
                mat[r][c] = count
                count += 1
            n -= 1
            for i in range(n):
                r += direction
                mat[r][c] = count
                count += 1
            m -= 1
            direction *= -1
        return mat