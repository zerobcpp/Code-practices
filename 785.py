# 785. Is Graph Bipartite?

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        g = {i : [] for i in range(n)}
        
        for i, v in enumerate(graph):
            g[i].extend(v)
        seen = {}
        
        def helper(node, c):
            for neigh in g[node]:
                if neigh not in seen:
                    seen[neigh] = c
                    if not helper(neigh, -c):
                        return False
                else:
                    if seen[node] == seen[neigh]:
                        return False
            return True
        
        for i in range(n):
            if i not in seen:
                if not helper(i, 1):
                    return False
        #print(seen) 
        
        return True
    
    def isBipartitle(self, graph):
        n = len(graph)
        seen = {}
        st = []
        for i in range(n):
            if i in seen:
                continue
            st.append(i)
            seen[i] = 1
            while st:
                cur = st.pop()
                color = seen[i]
                for neigh in graph[i]:
                    if neigh not in seen:
                        seen[neigh] = -color
                        st.append(neigh)
                    elif seen[neigh] == seen[cur]:
                        return False
        
        return True
    