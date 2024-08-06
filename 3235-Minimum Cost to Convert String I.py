class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[float('inf')] * 26 for _ in range(26)]
        N = len(cost)
        for i in range(N):
            u, v, w = original[i], changed[i], cost[i]
            ori, cge = ord(u) - ord('a'), ord(v) - ord('a')
            graph[ori][cge] = min(graph[ori][cge], w)
        
        
        
        dist = [[float('inf')] * 26 for _ in range(26)]
        def helper(start):
            dist[start][start] = 0
            st = [(0, start)]
            
            while st:
                cost, cur = heappop(st)
                for j in range(26):
                    if graph[cur][j] != float('inf'):
                        if graph[cur][j] + cost < dist[start][j]:
                            new_cost = graph[cur][j] + cost
                            dist[start][j] = new_cost
                            heappush(st, (new_cost, j))
        
        for i in range(26):
            helper(i)
        
        #print(dist[2], graph[2])
        
        res = 0
        for i in range(len(source)):
            s, t = ord(source[i]) - ord('a'), ord(target[i]) - ord('a')
            if dist[s][t] == float('inf'):
                return -1
            #print(s, t)
            res += dist[s][t]
            #print(res)
        
        return res
            