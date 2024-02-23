class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        res = set()
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def helper(node):
            seen = set([node])
            stack = [node]
            while stack:
                cur = stack.pop()
                for nei in graph[cur]:
                    if nei not in seen:
                        stack.append(nei)
                        seen.add(nei)
            
            for i in range(n):
                if i not in seen:
                    if (node, i) not in res and (i, node) not in res:
                        res.add((node, i))
        
        for i in range(n):
            helper(i)
        return len(res)

