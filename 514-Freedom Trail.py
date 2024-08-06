class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        res = []
        N = len(ring)
        target = len(key)
        
        
        @cache    
        def helper(rotate, current):
            if current >= target:
                return 0
            
            cnt = float('inf')
            for i in range(N):
                if ring[i] == key[current]:
                    cw = abs(rotate - i)
                    acw = N - cw
                    cnt = min(cnt, min(cw, acw) + helper(i, current+1) + 1)
            
            return cnt
        
        return helper(0,0)
    
    
    
    
    
    
    #min(min_steps, count_steps(ring_index, char_index) + 1  + try_lock(char_index, key_index + 1))