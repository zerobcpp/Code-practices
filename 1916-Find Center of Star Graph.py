class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
            if len(graph[u]) == n:
                return u
            if len(graph[v]) == n:
                return v
        
        return -1