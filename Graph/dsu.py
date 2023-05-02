class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * (n)
        
    def find(self, x):
        temp = x
        while x != self.parent[x]:
            x = self.parent[x]
        self.parent[temp] = x
        return x
    
    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return 0
        if self.rank[xp] > self.rank[yp]:
            self.parent[yp] = xp
        elif self.rank[yp] > self.rank[xp]:
            self.parent[xp] = yp
        else:
            self.parent[yp] = xp
            self.rank[xp] += 1
        return 1
    
    
    