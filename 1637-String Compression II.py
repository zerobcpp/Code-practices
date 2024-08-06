class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        N = len(s)
        @cache
        def helper(i, prev, cnt, left):
            if i >= N:
                return 0
            delete = float('inf')
            
            if left > 0:
                delete = helper(i+1, prev, cnt, left-1)
                
            keep = 0
            if s[i] == prev:
                digit = 0
                if len(str(cnt+1)) > len(str(cnt)) or cnt == 1:
                    digit = 1
                
                keep = helper(i+1, s[i], cnt+1, left) + digit
            else:
                keep = helper(i+1, s[i], 1, left) + 1
                
                
            #print(keep, delete)
            return min(keep, delete)
        
        return helper(0, '', 0, k)