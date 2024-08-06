class Solution:
    def specialArray(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        
        for i in range(N):
            left = bisect_left(nums, i+1)
            #right = bisect_right(nums, i+1)
            #print(left, right, i)
            
            if N - left == i + 1:
                #print(N-left, i+1)
                return i + 1
            
        
        return -1
    
    
    
    [0,3,4,6,6,7]
        