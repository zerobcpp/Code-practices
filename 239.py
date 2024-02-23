class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        N = len(nums)
        window = deque()
        
        l = 0
        for r in range(N):
                
            window.append(nums[r])
            if len(window) >= k:
                res.append(max(window))
                window.popleft()
            
            #print(window)
        
        return res