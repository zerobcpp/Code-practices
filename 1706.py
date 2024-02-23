class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {0: 0}
        seen = set()
        st = [(0, 0)]
        res = 0
        N = len(points)
        while st:
            n, w = heappop(st)
            
            if n in seen:
                continue
            if n in graph:
                if graph[n] > w:
                    continue
            seen.add(n)
            res += w
            x, y = points[n]
            
            for i in range(N):
                dx, dy = points[i]
                if i not in seen:
                    dist = abs(x-dx) + abs(y - dy)
                    
                    if dist < graph.get(i, float('inf')):
                        heappush(st, (i, dist))
                        graph[i] = dist
        print(graph)
        return res