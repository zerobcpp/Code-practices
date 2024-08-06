class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        N = len(s)
        s.sort(reverse = True)
        cur = 0
        res = 0
        for i in s:
            cur += i
            if cur > 0:
                res += cur
            #print(res, cur)
        
        return res


    def maxSatisfactionC(self, s: List[int]) -> int:
        N = len(s)
        s.sort()
        c = {}
        def helper(time, idx):
            if idx == N:
                return 0
            if (time, idx) in c:
                return c[time, idx]
            
            c[(time, idx)] = max(s[idx] * time + helper(time+1, idx+1), 
                        helper(time, idx+1))
        
            return c[time, idx]
        helper(1, 0)
        return c[1, 0]


    def maxSatisfactionCache(self, s: List[int]) -> int:
        N = len(s)
        s.sort()
        @cache
        def helper(time, idx): 
            if idx == N:
                return 0

            return max(s[idx] * time + helper(time+1, idx+1), 
                        helper(time, idx+1))
        
        return (helper(1, 0))
