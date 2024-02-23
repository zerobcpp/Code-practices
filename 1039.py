class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = {i+1 : [] for i in range(n)}
        
        for u, v in trust:
            graph[u].append(v)
        
        for i, v in graph.items():
            if len(v) == 0:
                return i
        
        return -1