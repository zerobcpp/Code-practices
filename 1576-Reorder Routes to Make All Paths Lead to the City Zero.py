class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        E = [(i, o) for i, o in connections]
        for u, v in connections:
            graph[u].append((v,1))
            graph[v].append((u,0))
        res = 0
        seen = set([0])
        stack = deque([0])
        
        while stack:
            cur = stack.popleft()
            for neigh, temp in graph[cur]:
                if (neigh, cur) not in E and neigh not in seen:
                    res += 1    
                if neigh not in seen:
                    seen.add(neigh)
                    stack.append(neigh)
        
        return res