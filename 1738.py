class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                rank = len(graph[i] + graph[j])
                if i in graph[j]:
                    rank -= 1
                res = max(res, rank)
        
        return res