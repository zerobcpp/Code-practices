class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = {i+1 : 0 for i in range(n)}
        
        for u, v in trust:
            graph[v] += 1
            graph[u] -= 1
        
        #print(graph)
        for i, v in graph.items():
            if v == n - 1:
                return i
            
        return -1
    
    
    
    # judge should have n - 1 incoming edge
    # other don't care