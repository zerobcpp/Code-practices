# 441. Arranging Coins
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            mid = l + (r - l) // 2
            coin = (mid * (mid + 1)) // 2
            if coin == n:
                return mid
            if n < coin:
                r = mid - 1
            else:
                l = mid + 1
        
        return r