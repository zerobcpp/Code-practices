class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        c = [[w/q, w, q] for w, q in zip(wage, quality)]
        tq = sum(quality)
        c.sort()
        tc = float('inf')
        cq = 0
        st = []
        
        for i in c:
            qdx, w, q = i
            cq += q
            heappush(st, -q)
            while len(st) > k:
                x = heappop(st)
                cq += x
            
            if len(st) == k:
                #print(st, cq, qdx)
                tc = min(tc, cq * qdx)
            
            
        
        return tc
                