class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {i: [] for i in range(n)}
        adj = [0] * n
        for u, v in edges:
            graph[v].append(u)
            adj[v] += 1
        
        #print(graph, adj)
        res = [[] for _ in range(n)]
        #st = [(i, -1) for i in range(n) if adj[i] == 0]
        
        for i in range(n):
            st = [(i)]
            seen = set()
            while st:
                cur = st.pop()
                
                for neigh in graph[cur]:
                    if neigh not in seen:
                        seen.add(neigh)
                        st.append(neigh)
            
            res[i].extend(list(sorted(seen)))
                    
        return res
        