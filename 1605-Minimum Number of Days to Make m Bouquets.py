class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        

        res = 0
        def can(mid):
            cnt = 0
            flower = 0
            for i in bloomDay:
                if i <= mid:
                    cnt += 1
                else:
                    cnt = 0
                
                if cnt >= k:
                    flower += 1
                    cnt = 0
            
            return flower
        
        l = 0
        r = max(bloomDay)
        res = float('inf')
        while l <= r:
            mid = l + (r - l) // 2
            #print(mid)
            if can(mid) >= m:
                r = mid - 1
                res = min(res, mid)
            else:
                l = mid + 1
        
        return res
            