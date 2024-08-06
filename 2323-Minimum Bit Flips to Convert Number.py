class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        print(f'{bin(start)[2:]:0>8}')
        print(f'{bin(goal)[2:]:0>8}')
        
        res = 0
        while start or goal:
            gbit = goal & 1
            sbit = start & 1
            if gbit ^ sbit == 1:
                res += 1
            start >>= 1
            goal >>= 1
        
        return res