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
    
    
    def maxCoins(self, piles):
        piles.sort()
        res = 0
        N = len(piles)
        print(piles)
        for i in range(N//3, N, 2):
            res += piles[i]
        
        return res
            