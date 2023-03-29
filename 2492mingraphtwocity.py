class Solution:
    def minScore(self, n: int, roads):
        res = float('inf')
        stack = [1]
        seen = set([1])
        graph = {i: [] for i in range(1, n + 1)}
        for i, o, cost in roads:
            graph[i].append((o, cost))
            graph[o].append((i, cost))

        while stack:
            cur = stack.pop()
            # print(cur, path)
            for neigh, cost in graph[cur]:
                res = min(res, cost)
                if neigh not in seen:
                    seen.add(neigh)
                    stack.append((neigh))

        return res
