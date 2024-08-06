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
    
    
    def destCity(self, paths):
        graph = defaultdict(list)
        for u, v in paths:
            graph[u].append(v)
            
        start = [paths[0][0]]
        
        while start:
            cur = start.pop()
            
            for neigh in graph[cur]:
                start.append(neigh)
        
        return cur
    
    
    def destCity(self, paths):
        seen = set()
        for u, v in paths:
            seen.add(u)
        
        for u, v in paths:
            if v not in seen:
                return v
        
        return -1