class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = {i : [] for i in range(n)}
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        restricted = set(restricted)
        st = [0]
        res = []
        seen = set([0])
        
        while st:
            cur = st.pop()
            res.append(cur)
            for neigh in graph[cur]:
                if neigh not in restricted and neigh not in seen:
                    st.append(neigh)
                    seen.add(neigh)
        
        return len(res)
                