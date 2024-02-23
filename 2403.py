class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        seen = set()
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def helper(node):
            stack = [node]
            count = 0
            seen.add(node)
            while stack:
                cur = stack.pop()
                count += 1
                for nei in graph[cur]:
                    if nei not in seen:
                        stack.append(nei)
                        seen.add(nei)
            return count

        
        for i in range(n):
            if i not in seen:
                cur = helper(i)
                res += cur * (n - cur)
                n -= cur
        return res

