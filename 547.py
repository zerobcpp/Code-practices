#547. Number of Provinces

class Solution:
    def findCircleNumItr(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        res = 0
        st = []
        seen = set()
        
        for i in range(n):
            if i not in seen:
                st.append(i)
                seen.add(i)
                while st:
                    cur = st.pop()
                    
                    for j in range(n):
                        if isConnected[cur][j] == 1 and j not in seen:
                            st.append(j)
                            seen.add(j)
                res += 1
        return res
    
    def findCircleNumRecur(self, isConnected):
        n = len(isConnected)
        seen = set()
        def helper(node):
            if node in seen:
                return
            seen.add(node)
            for i in range(n):
                if isConnected[node][i]:
                    helper(i)
        res = 0
        for i in range(n):
            if i not in seen: 
                helper(i)
                res += 1
        
        return res
    
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        uf = DSU(n)
        res = n
        
        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    res -= uf.union(i, j)
        
        #print(uf.parent, uf.rank)
        return res
    
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * (n)
        
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
    
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
    
    
    