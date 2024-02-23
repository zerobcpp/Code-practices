class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        st = deque([(1 << i, i, 0) for i in range(n)])
        seen = set((1 << i, i) for i in range(n))
        #print((1 << n)-1)
        
        while st:
            mask, node, res = st.pop()
            
            if mask == (1 << n) - 1:
                return res
            
            for neigh in graph[node]:
                temp = mask | ( 1 << neigh)
                if (temp, neigh) not in seen:
                    seen.add((temp, neigh))
                    st.append((temp, neigh, res + 1))
        
        return -1
    
