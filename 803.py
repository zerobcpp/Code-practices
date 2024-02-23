class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 10 ** 7
        dest =  [[INF] * (k+2) for _ in range(n)]
        graph = defaultdict(list)
        for u, v, p in flights:
            graph[u].append((v, p))
        
        dest[src][k+1] = 0
        st = [(0, src, k+1)]
        while st:
            weight, cur, left = heappop(st)
            if cur == dst:
                return weight
            if left <= 0:
                continue
            for neigh, cost in graph[cur]:
                new_weight = weight + cost
                #print(left-1, neigh)
                if new_weight < dest[neigh][left-1]:
                    dest[neigh][left-1] = new_weight
                    heappush(st, (new_weight, neigh, left - 1))
        
        
        return dest[dst][0] if dest[dst][0] != INF else -1
            