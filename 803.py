class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 10 ** 5
        dest =  [INF] * n
        graph = defaultdict(list)
        
        for u, v, p in flights:
            graph[u].append((v, p))
        
        dest[src] = 0
        st = [(0, src, k+1)]
        
        while st:
            weight, cur, left = heappop(st)
            if left <= 0:
                continue
            for neigh, cost in graph[cur]:
                new_weight = weight + cost
                if new_weight <= dest[neigh]:
                    dest[neigh] = new_weight
                    heappush(st, (new_weight, neigh, left - 1))
            #print(st, dest)
        
        return dest[dst]
            