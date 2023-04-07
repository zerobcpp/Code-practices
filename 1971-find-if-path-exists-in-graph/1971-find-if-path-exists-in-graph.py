class Solution:
    def validPath1(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = {i : [] for i in range(n)}
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        st = [source]
        seen = [0] * n
        seen[source] = 1
        while st:
            start = st.pop()
            if destination == start:
                return True
            
            for neigh in g[start]:
                if seen[neigh] == 0:
                    st.append(neigh)
                    seen[neigh] = 1
        
        return False
    
    
    def validPath(self, n, edges, source, destination) -> bool:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        print(uf.root, uf.rank)
        return uf.find(source) == uf.find(destination)
                
        
class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n
    def find(self, x):
        while self.root[x] != x:
            self.root[x], x = self.root[self.root[x]], self.root[x]
        return x
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if (self.rank[xr] < self.rank[yr]): # Make yr parent of xr
            self.root[xr] = self.root[yr]
            self.rank[yr] += self.rank[xr]
        else: # Make xr parent of yr
            self.root[yr] = self.root[xr]
            self.rank[xr] += self.rank[yr]