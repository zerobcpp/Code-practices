class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        g = {i : [] for i in range(N)}
        adj = [0] * N
        for i, v in enumerate(graph):
            for o in v:
                g[o].append(i)
                adj[i] += 1
        
        print(g)
        print(adj)
        st = [i for i in range(N) if not adj[i]]
        
        seen = set()
        while st:
            cur = st.pop()
            #res.append(cur)
            for neigh in g[cur]:
                adj[neigh] -= 1
                if not adj[neigh]:
                    st.append(neigh)
        
        return [i for i in range(N) if not adj[i]]