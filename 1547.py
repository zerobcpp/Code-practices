class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = defaultdict(list)
        
        for u, v in paths:
            graph[u].append(v)
            
        
        for u, v in paths:
            if u not in graph:
                return u
            if v not in graph:
                return v
        
        return -1