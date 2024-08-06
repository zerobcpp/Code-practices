class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        N = len(garbage)
#         t = []
#         for trash in garbage:
#             temp = Counter(trash)
#             metal = temp['M']
#             paper = temp['P']
#             glass = temp['G']
#             t.append((metal, paper, glass))
        
#         for i in range(N-1, -1, -1):
#             nxt, cur = t[i-1]
#             for i in range(3):
                
        mp = 0
        pp = 0
        gp = 0
        mi = pi = gi = None
        travel = [0] + travel
        T = []
        for i in range(N):
            m = p = g = 0
            for t in garbage[i]:
                
                if t == 'M':
                    m += 1
                    mi = i
                elif t == 'P':
                    p += 1
                    pi = i
                else:
                    g += 1
                    gi = i
            mp += (travel[i] + m)
            pp += (travel[i] + p)
            gp += (travel[i] + g)
            T.append((mp, pp, gp))
        
        #print(mi, pi, gi)
        #print(T)
        res = 0
        if pi != None:
            res += T[pi][1]
        if gi != None:
            res += T[gi][2]
        if mi != None:
            res += T[mi][0]
        
        return res
                
            
                
           # metal, paper, glasss