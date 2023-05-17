# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            length = r - l
            area = length * h
            res = max(area, res)
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        
        return res