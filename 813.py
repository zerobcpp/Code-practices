class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        out = {}
        end = len(graph) - 1
        for i in range(len(graph)):
            out[i] = graph[i]
        res =[]
        stack = [(0, [0])]
        while stack:
            cur, arr = stack.pop()
            if cur == end:
                res.append(arr[:])
            for edge in out[cur]:
                stack.append((edge, arr+[edge]))
        return res
                