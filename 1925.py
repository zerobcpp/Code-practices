class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        c = defaultdict(int)
        def reverse(s):
            s = str(s)[::-1]
            return int(s)
        
        def rev(num):
            result = 0
            while num:
                result = result * 10 + num % 10
                num //= 10
            
            return result
        
        res = 0
        for i in nums:
            idx = i - rev(i)
            res = (res + c[idx]) % MOD 
            c[idx] += 1
        
        #print(c)
        return res 