class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        dpl = [0] * N
        dpr = [0] * N
        dpl[0] = height[0]
        dpr[-1] = height[-1]
        
        for i in range(1, N):
            dpl[i] = max(dpl[i-1],height[i-1])
        
        for i in range(N-2, -1,-1):
            dpr[i] = max(dpr[i+1], height[i+1])
        
        res = 0
        for i in range(N):
            res += max(min(dpl[i], dpr[i]) - height[i], 0)
        
        return res