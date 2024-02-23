class Solution:
    def findPaths(self, n: int, m: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dirs = [0, 1, 0, -1, 0]
        cache = {}
        
        def helper(i, j, move):
            if move < 0:
                return 0
            if (i >= n or j >= m or i < 0 or j < 0):
                return 1
            if (i, j, move) in cache:
                return cache[i, j, move]

            cnt = 0
            for idx in range(4):
                dx, dy = i + dirs[idx], j + dirs[idx+1]
                #print(dx, dy)
                cnt += helper(dx, dy, move-1)
                
            cache[i, j, move] = cnt
            return cnt
        
        
        return helper(startRow, startColumn, maxMove)