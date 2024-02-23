class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * (n)
        self.maxRank = 1
        
    def find(self, x):
        temp = x
        while x != self.parent[x]:
            x = self.parent[x]
        self.parent[temp] = x
        return x
    
    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return False
        if self.rank[xp] > self.rank[yp]:
            self.parent[yp] = xp
            self.rank[xp] += self.rank[yp]
        elif self.rank[yp] > self.rank[xp]:
            self.parent[xp] = yp
            self.rank[yp] += self.rank[xp]
        else:
            self.parent[yp] = xp
            self.rank[xp] += self.rank[yp]
        self.maxRank = max(self.maxRank, self.rank[xp], self.rank[yp])
        return True
        
    
    
    
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        temp = edges.copy()
        temp.sort(key = lambda x: x[2])
        uf = DSU(n)
        
        total_cost = 0
        for u, v, c in temp:
            if uf.union(u, v):
                total_cost += c
        
        #print(uf.rank, uf.parent)
        #print(total_cost)
        crit = [] # edge deletion causing increase MST cost
        pcrit = [] # edge that can be deleted but doesn't increase MST cost
        
        for i, (u, v, c) in enumerate(temp):
            uft = DSU(n)
            adjust = 0
            
            for j, (ju, jv, jc) in enumerate(temp):
                if i != j and uft.union(ju, jv):
                    adjust += jc
            
            if adjust > total_cost:
                crit.append(i)
                continue
            
            uft = DSU(n)
            adjust = c
            uft.union(u, v)
            for j, (ju, jv, jc) in enumerate(temp):
                if i != j and uft.union(ju, jv):
                    adjust += jc
            
            if adjust == total_cost:
                pcrit.append(i)
        
        
        return (crit, pcrit)
            
            