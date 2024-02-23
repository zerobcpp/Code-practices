class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = set(arr)
        MOD = 10 ** 9 + 7
        
        @cache
        def helper(i):
        
            res = 1
            for f in arr:
                if i % f == 0 and i // f in arr:
                    res += (helper(f) * helper(i//f))
            
            return res % MOD
        
        res = 0
        
        for i in arr:
            res += helper(i) % MOD
        
        return res
        
