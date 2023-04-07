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
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                root_x, root_y = root_y, root_x
            # Modify the root of the smaller group as the root of the
            # larger group, also increment the size of the larger group.
            self.rank[root_y] += self.rank[root_x]
            self.root[root_x] = root_y