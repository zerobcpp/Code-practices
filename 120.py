class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        adjacent = [0, 1]
        
        path = [0] * (n+1)
        path[1] = triangle[0][0]
        
        x = 0
        for y in range(1,n):
            if triangle[y][x] > triangle[y][x+1]:
                xidx = triangle[y].index(triangle[y][x+1])
            else:
                xidx = triangle[y].index(triangle[y][x ])
            step = triangle[y][xidx]
            path[y+1] = path[y] + step
            print(step)
        
        print(path)
        return path[n]
        
            