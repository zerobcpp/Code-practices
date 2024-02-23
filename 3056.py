class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x = sx + t
        y = sy + t
        
        return x >= fx and y >= fy