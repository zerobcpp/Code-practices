class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(n)}
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        mx = float('inf')
        res = []
        for i in range(n):
            st = deque([i])
            seen = set([i])
            level = 0
            while st:
                nst = len(st)
                for j in range(nst):
                    cur = st.popleft()
                    for neigh in graph[cur]:
                        if neigh not in seen:
                            st.append(neigh)
                            seen.add(neigh)
                
                level += 1
            #print(level)
            if level == mx:
                res.append(i)
            if level < mx:
                mx = level
                res = [i]
        
        return res
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            if n == 1:
                return [0]
            return None
        graph = {i: [] for i in range(n)}
        adj = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            adj[u] += 1
            adj[v] += 1
        
        #print(adj, graph)
        st = deque([i for i in range(n) if adj[i] == 1])
        res = []
        
        while st:
            res = []
            nst = len(st)
            for i in range(nst):
                cur = st.popleft()
                res.append(cur)
                
                for neigh in graph[cur]:
                    adj[neigh] -= 1
                    if adj[neigh] == 1:
                        st.append(neigh)
        
        return res
            
        