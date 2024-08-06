class Solution:
    def reorganizeString(self, s: str) -> str:
        c = {}
        for i in s:
            c[i] = c.get(i, 0) + 1
        
        count = [[v, i] for i, v in c.items()]
        count.sort(reverse = True)
        count = deque(count)
        n = len(count)
        res = []
        
        while count:
            print(count)
            most = count[0][1]
            count[0][0] -= 1
            least = None
            if len(count) != 1:
                least = count[-1][1]
                count[-1][0] -= 1
                
            if least:
                res.extend([most, least])
            else:
                res.append(most)
            
            while count and count[0][0] == 0:
                count.popleft()
            while count and count[-1][0] == 0:
                count.pop()
            
            print(res)
            if res[-1] == res[-2]:
                return ''
        
        return ''.join(res)
    
    
    def reorganizeString(self, s: str) -> str:
        c = {}
        for i in s:
            c[i] = c.get(i, 0) + 1
        
        count = [(-v, i) for i, v in c.items()]
        heapify(count)
        res = []
        
        while count:
            mf, mc = heappop(count)
            #print(count)
            if not res or res[-1] != mc:
                res.append(mc)
                if mf+1 != 0:
                    heappush(count, (mf+1, mc))
            else:
                if not count:
                    return ''
                lf, lc = heappop(count)
                res.append(lc)
                if lf + 1 != 0:
                    heappush(count, (lf+1, lc))
                heappush(count, (mf, mc))
            
            
        
        return ''.join(res)
            