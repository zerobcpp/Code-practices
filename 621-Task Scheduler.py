class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:        
        c = defaultdict(int)
        for i in tasks:
            c[i] += 1
        
        heap = [-i for i in c.values() if i > 0]
        events = deque()
        heapify(heap)
        res = 0
        while heap or events:
            res += 1
            if heap:
                cur = -heappop(heap)
                if cur - 1 != 0:
                    events.append([res + n, cur-1])

            
            while events and events[0][0] <= res:
                _, left = events.popleft()
                heappush(heap, -left)
            
            #print(heap)
            #print(events, res)
        
        return res
                
                
                