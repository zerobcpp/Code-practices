class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], k: int) -> int:
        graph = {i : [] for i in range(n)}
        
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])
        
        ret = -1
        reach = float('inf')
        res = [[] for i in range(n)]
        print(graph)
        for i in range(n):
            st = [(i, k)]
            seen = set()
            while st:
                cur, left = st.pop()
                for neigh, cost in graph[cur]:
                    if neigh not in seen and left - cost >= 0 and neigh != i:
                        st.append([neigh, left - cost])
                        seen.add(neigh)
                if i == 5:
                    print(st)
            
            
            if len(seen) <= reach:
                if i > ret:
                    ret = i
                    reach = min(reach, len(seen))
            print(seen, i, reach, ret)
        return ret
    
    
    def findTheCity(self, n, edges, k):
        graph = {i: [] for i in range(n)}
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])
        
        dist = [[float('inf')] * n for _ in range(n)]
            
        def helper(start):
            st = [start]
            dist[start][start] = 0
            seen = set()
            while st:
                cur = st.pop()
                for neigh, cost in graph[cur]:
                    if neigh not in seen:
                        if dist[start][neigh] > dist[start][cur] + cost:
                            dist[start][neigh] = dist[start][cur] + cost
                            st.append(neigh)
        
        cur = float('inf')
        ret = 0
        reach = [0] * n
        for i in range(n):
            helper(i)
            cnt = 0
            for j in dist[i]:
                if j <= k:
                    cnt += 1
            reach[i] = cnt
        
        for i in range(n):
            if cur >= reach[i]:
                cur = reach[i]
                ret = i
                
        return ret
                        
                        