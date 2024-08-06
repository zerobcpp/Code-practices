class Solution:
    def restoreArray(self, adjPairs: List[List[int]]) -> List[int]:
        N = len(adjPairs)
        g = defaultdict(list)
        
        
        for u, v in adjPairs:
            g[u].append(v)
            g[v].append(u)
        #    adj[u] += 1
        #print(g)
        st = []
        for i, v in g.items():
            if len(v) == 1:
                st.append(i)
                break
        
        res = []
        seen = set(st)
        #print(st)
        while st:
            cur = st.pop()
            res.append(cur)
            
            for neigh in g[cur]: 
                if neigh not in seen:
                    st.append(neigh)
                    seen.add(neigh)
                
            
        
        return res