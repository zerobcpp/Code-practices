class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = defaultdict(list)
        self.n = n
        
        for u, v, c in edges:
            self.g[u].append((v, c))
        print(self.g)

    def addEdge(self, edge: List[int]) -> None:
        u, v, c = edge
        self.g[u].append((v,c))

    def shortestPath(self, node1: int, node2: int) -> int:
        cost = [float('inf')] * self.n
        cost[node1] = 0
        st = [(0, node1)]
        
        while st:
            cc, cx = heappop(st)
            
            if cc > cost[cx]:
                continue
            if cx == node2:
                return cc
            
            for neigh in self.g[cx]:
                nx, nc = neigh
                #print(nc, nx, cost)
                if nc + cc < cost[nx]:
                    cost[nx] = nc + cc
                    heappush(st, (nc+cc, nx))
        
        return -1
                
                


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)