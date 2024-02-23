class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = deque(piles)
        res = 0
        
        while piles:
            x, y = piles.pop(), piles.pop() 
            r = piles.popleft()
            res += y
        
        return res