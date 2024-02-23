class Solution:
    def minimumTime(self, n: int, R: List[List[int]], time: List[int]) -> int:
        graph = {i : [] for i in range(1,n+1)}
        adj = [0] * (n+1)
        
        for u, v in R:
            adj[v] += 1
            graph[u].append(v)
        
        #print(graph, adj)
        st = deque([i for i in range(1, n+1) if adj[i] == 0])
        res = [0] * (n+1)
        
        for i in range(1, n+1):
            res[i] = time[i-1]
            
        while st:
            cur = st.popleft()
            for neigh in graph[cur]:
                adj[neigh] -= 1
                res[neigh] = max(res[neigh], res[cur] + time[neigh-1])
                if not adj[neigh]:
                    st.append(neigh)
                    
        
        
        return max(res)
                