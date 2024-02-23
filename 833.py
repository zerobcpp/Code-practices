class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        for i, route in enumerate(routes):
            for j in route:
                graph[j].append(i)
                
        print(graph)
        st = deque([(source, 0)])
        seen = set()
        seen.add(source)
        #r_seen = set()
        while st:
            cur, stop = st.popleft()
            if cur == target:
                return stop
            for idx in graph[cur]:
                if routes[idx]:
                    for bus in routes[idx]:
                        if bus not in seen:
                            seen.add(bus)
                            st.append((bus, stop + 1))
                    #r_seen.add(idx)
                routes[idx] = []
            
        
        return -1