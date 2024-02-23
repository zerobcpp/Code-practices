class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False
        x = abs(sx - fx)
        y = abs(sy - fy)
        #print(x, y)
        return max(x,y) <= t