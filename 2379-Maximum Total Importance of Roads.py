class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i in range(n):
            graph[i] = []
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        st = []
        for i, v in graph.items():
            heappush(st, [len(v), i])
            
        res = 0
        i = 0
        while st:
            v, _ = heappop(st)
            res += (i + 1) * v 
            i += 1
        
        return res
    
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = [0] * n
        
        for u, v in roads:
            graph[u] += 1
            graph[v] += 1
        
        graph.sort()
        res = 0
        for i in range(n):
            res += (i + 1) * graph[i]
        
        return res
    
            
        
        
