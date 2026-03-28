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
    
    def __str__(self):
        return f"Parent: {self.parent}\nRank: {self.rank}\nMaxRank: {self.maxRank}"
        