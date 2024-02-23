class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        N = len(corridor)
        cache = [[-1] * 3 for _ in range(N)]
        #print(cache)
        def helper(i, chair):
            if i >= N:
                if chair == 2:
                    return 1
                return 0
            if cache[i][chair] != -1:
                return cache[i][chair]
            if chair > 2:
                return 0
            if corridor[i] == 'S':
                chair += 1
            ns = div = 0
            skip = helper(i+1, chair)
            if chair == 2:
                ns = helper(i+1, chair)
                div = helper(i+1, 0)
                
            
            cache[i][chair] = max(skip, div+ns) % MOD  
            return cache[i][chair]
                
                
        
        return helper(0, 0)
    
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        N = len(corridor)
        @cache
        def helper(i, chair):
            if i >= N:
                if chair == 2:
                    return 1
                return 0
            if chair > 2:
                return 0
            if corridor[i] == 'S':
                chair += 1

            ns = div = 0
            skip = helper(i+1, chair)
            if chair == 2:
                ns = helper(i+1, chair)
                div = helper(i+1, 0)
            
            return max(skip, ns+div) % MOD
                
                
        
        return helper(0, 0)
        