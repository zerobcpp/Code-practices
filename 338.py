class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        
        for i in range(n+1):
            cnt = 0
            while i:
                i &= (i-1)
                cnt += 1
            res.append(cnt)
            #print(i, cnt)
        
        return res
        
    
    def countBits(self, n):
        cache = {}
        def helper(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i in cache:
                return cache[i]
            count = 0
            if i % 2 == 0:
                count = helper(i // 2)
            else:
                count = 1 + helper(i // 2)
            
            cache[i] = count
            return count
        res = []
        for i in range(n+1):
            res.append(helper(i))
        
        return res