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
        return f"Parent: {self.parent}\nRank:   {self.rank}\nMaxRank: {self.maxRank}"
        
        
def convert_list(arr, toInt = False):
    N = len(arr)
    for i in range(N):
        if toInt:
            arr[i] = [int(j) for j in inputs[i].split(',')]
        else:
            arr[i] = list(arr[i])
    return arr

def d8(x, y):
    cords = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i or j:
                cords.append((x+i, y+j))
    return cords

d4 = [0, -1, 0, 1, 0]
dr = {
    0: [0, -1], #<
    1: [-1, 0], #^
    2: [0, 1],  #>
    3: [1, 0],  #v
}

from collections import defaultdict
from sortedcontainers import SortedList


with open('d8.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')
convert_list(inputs, True)

#print(*inputs, sep = '\n')
N = len(inputs)
for i, v in enumerate(inputs):
    print(i, v)

c = defaultdict(SortedList)
cc = SortedList()
for i in range(N):
    px, py, pz = inputs[i]
    
    for j in range(i+1, N):
        if i == j:
            continue
        qx, qy, qz = inputs[j]
        dist = ((px - qx) ** 2 + (py - qy) ** 2 + (pz - qz) ** 2) ** 0.5
        c[i].add((dist, j))        
        cc.add((dist, i, j))

used = set()
graph = defaultdict(set)
dsu = DSU(N)
#print(cc)
for i in range(10):
    d, u, v = cc.pop(0)
    dsu.union(u, v)
    

for i in range(N):
    graph[dsu.find(i)].add(i)

p1 = sorted([len(graph[i]) for i in graph])[::-1]
res = 1
for i in range(3):
    res *= p1[i]


#print(res)
# p2 - connecting the remaining

for d, u, v in cc:
    dsu.union(u, v)
    #print(dsu, inputs[u], inputs[v])
    if dsu.maxRank == N:
        print(dsu, inputs[u], inputs[v])
        break


# both dsu problem.