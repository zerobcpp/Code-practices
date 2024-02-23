class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        c = defaultdict(int)
        def reverse(s):
            s = str(s)[::-1]
            return int(s)
        
        res = 0
        for i in nums:
            idx = i - reverse(i)
            res += c[idx]
            c[idx] += 1
        
        #print(c)
        return res 