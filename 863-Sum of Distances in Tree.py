class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        depth = [0] * n
        res = [0] * n
        cnt = [0] * n
        
        def helper(node, parent, deep):
            ways = 1
            for neigh in graph[node]:
                if neigh != parent:
                    ways += helper(neigh, node, deep+1)
                    
            depth[node] = deep
            cnt[node] = ways
            return ways
        
        def helper2(node, parent, tot):
            
            for neigh in graph[node]:
                if neigh != parent:
                    helper2(neigh, node, tot + n - 2*cnt[neigh])
            res[node] = tot
                    
        helper(0, -1, 0)
        helper2(0, -1, sum(depth))
        
        print(depth, res, cnt)
        return res