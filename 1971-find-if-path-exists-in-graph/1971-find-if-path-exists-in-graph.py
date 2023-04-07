class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = {i : [] for i in range(n)}
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        st = [source]
        seen = [0] * n
        seen[source] = 1
        while st:
            start = st.pop()
            if destination == start:
                return True
            
            for neigh in g[start]:
                if seen[neigh] == 0:
                    st.append(neigh)
                    seen[neigh] = 1
        
        return False
                