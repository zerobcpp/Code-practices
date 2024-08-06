class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x2 = x1 = mask = 0
        for i in nums:
            x2 ^= x1 & i
            x1 ^= i
            mask = ~(x1&x2)
            x2 &= mask
            x1 &= mask
        
        return x1
    
    
    def singleNumber(self, nums):
        c = Counter(nums)
        for i in c:
            if c[i] != 3:
                return i
        
        return -1