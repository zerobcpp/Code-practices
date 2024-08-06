class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = defaultdict(int)
        for i in arr:
            c[i] += 1
        
        data = defaultdict(list)
        
        for i, v in c.items():
            data[v].append(i)
        
        mx = max(data.keys())
        unique = len(c)
        done = False
        for i in range(1, mx + 1):
            
            if i in data:
                for num in data[i]:
                    if k - i >= 0:
                        k -= i
                        unique -= 1
                    else:
                        done = True
                
                if done:
                    break
        
        return unique
    
    
    def findLeastNumOfUniqueInts(self, arr, k):
        c = {}
        
        for i in arr:
            c[i] = c.get(i, 0) + 1
        
        heap = list(c.values())
        heapify(heap)
        unique = len(c)
        #print(unique, c, heap)
        while heap:
            cur = heappop(heap)
            if k - cur < 0:
                return unique
            k -= cur
            unique -= 1
        
        return 0
        
    # [4,3,1,1,3,3,2]
    # [1,1,2,3,3,3,4]