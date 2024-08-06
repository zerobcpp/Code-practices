class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def helper(mid):
            req = mid * n
            cur = 0
            for i in batteries:
                if i < mid:
                    cur += i
                else:
                    cur += mid
            
            #print(cur, mid, req)
            return cur >= req
        
        l, r = 0, sum(batteries) // n + 1
        res = 0
        while l <= r:
            mid = l + (r - l) // 2
            if helper(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return res