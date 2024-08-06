class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = {i: [] for i in range(1, n+1)}
        def helper(i, o):
            seen = set([i])
            stack = [i]
            while stack:
                start = stack.pop()
                if start == o:
                    return False
                
                for neigh in graph[start]:
                    if neigh not in seen:
                        stack.append(neigh)
                        seen.add(neigh)
            
            return True
        
        for u, v in edges:
            if u in graph and v in graph:
                if not helper(u, v):
                    return [u, v]
            
            graph[u].append(v)
            graph[v].append(u)
        
        return [-1,-1]
    
