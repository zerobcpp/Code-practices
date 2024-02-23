class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        
        @cache
        def helper(i):
            if i >= N:
                return 0
            
            mx = 0
            j = i
            cnt = 0
            length = 0
            while length < k and j < N:
                mx = max(mx, arr[j])
                length += 1
                j += 1
                cnt = max(cnt, mx * length + helper(j))
                
            return cnt
        
        return helper(0)
            
            
            
                
                
            
        
        
        
        
        
        
        
        
        #1,4,1,5,7,3,6,1,9,9,3
        #1,7,7,7,7,9,9,9,9,9,9 = 83
        