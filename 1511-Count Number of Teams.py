class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        @cache
        def helper(i, cnt):
            if cnt == 3:
                return 1
            if i >= N:
                return 0
            
            take = 0
            for idx in range(i+1, N):
                if rating[idx] > rating[i]:
                    take += helper(idx, cnt+1)

            return take
        @cache
        def helper2(i, cnt):
            if cnt == 3:
                return 1
            if i >= N:
                return 0
            take = 0
            for idx in range(i+1, N):
                if rating[idx] < rating[i]:
                    take += helper2(idx, cnt+1)

            return take
        
        res = 0
        for i in range(N):
            res += helper(i, 1)
            res += helper2(i, 1)
        return res
    
    
    def numTeams(self, rating):
        res = 0
        N = len(rating)
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1,N):
                    if rating[i] > rating[j] > rating[k] or rating[i] < rating[j] < rating[k]:
                        res += 1
        
        return res
        
