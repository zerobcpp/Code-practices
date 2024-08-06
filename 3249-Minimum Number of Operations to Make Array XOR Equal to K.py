class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        end = k
        print(f'{bin(k)[2:]:0>8}')
        
        for i in nums:
            end ^= i
            #print(f'{bin(end)[2:]:0>8}')
        
        res = 0
        while end:
            if end | 1 == end:
                res += 1
            end >>= 1
        
        return res
        
        