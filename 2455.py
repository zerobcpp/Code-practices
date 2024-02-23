class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        N = len(edges)
        graph = {i:[] for i in range(N)}
        
        for i in range(N):
            source = edges[i]
            graph[source].append(i)
        
        res = 0
        idx = 0
        #print(graph)
        for i, v in graph.items():
            if sum(v) > res:
                res = sum(v)
                idx = i
        
        return idx