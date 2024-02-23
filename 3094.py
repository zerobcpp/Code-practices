class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = defaultdict(int)
        
        for i in nums:
            c[i] += 1
        
        res = 0
        
        for i, v in c.items():
            if v == 1:
                return -1
            
            while v > 4:
                res += 1
                v -= 3
            
            res += v // 2
        
        return res