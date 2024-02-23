class Solution:
    def numberOfWays(self, corridor: str) -> int:
        N = len(corridor)
        @cache
        def helper(i, chair):
            if i >= N:
                if chair == 2:
                    return 1
                return 0
            
            if corridor[i] == 'S':
                chair += 1
            ns = div = 0
            skip = helper(i+1, chair)
            if chair == 2:
                ns = helper(i+1, chair)
                div = helper(i+1, 0)
            
            return max(skip, ns+div)
                
                
        
        return helper(0, 0)
        