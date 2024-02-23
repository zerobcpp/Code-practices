class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        l = 1
        r = n
        while l <= r:
            mid = l + (r - l) // 2
            coin = (mid * (mid + 1)) // 2
            if coin >= n:
                r = mid - 1
            else:
                l = mid + 1
        
        return l - 1