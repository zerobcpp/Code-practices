class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        
        g = {i : [] for i in range(n)}
        node = {}
        for u,v in edges:   
            g[u].append(v)
        i = 0
        for c in colors:
            node[i] = c
            i += 1
        
        seen = set()
        st = [0]
        res = {}
        while st:
            cur = st.pop()
            res[node[cur]] = res.get(node[cur],0) + 1
            if cur in seen:
                return -1
            seen.add(cur)
            
            for neigh in g[cur]:
                st.append(neigh)
        
        return max(res.values())