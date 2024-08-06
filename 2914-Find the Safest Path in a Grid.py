class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        dist = [0, 1, 0, -1, 0]
        INF = 1000
        N = len(grid)
        M = len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        
        location = [[INF] * M for _ in range(N)]
        st = deque()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    st.append((i, j, 0))
                    location[i][j] = 0
                else:
                    location[i][j] = -1
        
        
        while st:
            n = len(st)
            for _ in range(n):
                x, y, danger = st.popleft()
                
                for i in range(4):
                    dx, dy = x + dist[i], y + dist[i+1]
                    if 0 <= dx < N and 0 <= dy < M and location[dx][dy] == -1:
                        location[dx][dy] = danger + 1
                        st.append((dx, dy, danger + 1))
        
        #print(location)
        st = [(-location[0][0], 0, 0)]
        res = []
        seen = set()
        seen.add((0, 0))
        while st:
            danger, x, y = heappop(st)
            if x == N-1 and y == M-1:
                return -danger
            for i in range(4):
                dx, dy = x + dist[i], y + dist[i+1]
                if 0 <= dx < N and 0 <= dy < M and (dx, dy) not in seen and grid[dx][dy] == 0:
                    heappush(st, (-min(-danger, location[dx][dy]),dx, dy))
                    seen.add((dx, dy))
        
        return 0
            
        
        
        