class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n+1)
        res = 0
        alice = 0
        bob = 0
        
        for t, u, v in edges:
            if t == 3:
                if dsu.union(u, v):
                    alice += 1
                    bob += 1
                else:
                    res += 1
        
        temp = dsu.parent[:]
        
        for t, u, v in edges:
            if t == 1:
                if dsu.union(u, v):
                    alice += 1
                else:
                    res += 1
        
        dsu.parent = temp
        
        for t, u, v in edges:
            if t == 2:
                if dsu.union(u, v):
                    bob += 1
                else:
                    res += 1    
        
        #print(a.rank, b.rank)
        #print(a.parent, b.parent)
        #print(alice, bob, res)
        return res if (alice == bob and bob == n - 1) else -1
        

        
class DSU:
    
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
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