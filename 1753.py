class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        st = [(0, 0, 0)]
        dirs = [0, 1, 0, -1, 0]
        res = [[10**6+1] * m for _ in range(n)]
        res[0][0] = 0
        #seen = set((0, 0))
        while st:
            diff, x, y = heappop(st)
            #seen.add((x, y))
            for i in range(4):
                dx, dy = x + dirs[i], y + dirs[i+1]
                #print(dx, dy)
                if 0 <= dx < n and 0 <= dy < m:
                    new_diff = max(diff, abs(heights[dx][dy] - heights[x][y]))
                    if new_diff < res[dx][dy]:
                        #if (dx, dy) not in seen:
                        res[dx][dy] = new_diff
                        heappush(st, (new_diff, dx, dy))

        
        return res[-1][-1]