class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowels = {
            'a' : 'e',
            'e' : 'ai',
            'i' : 'aeou',
            'o' : 'iu',
            'u' : 'a'
        }
        MOD = 10 ** 9 + 7
        @cache
        def helper(k, left):
            if left <= 0:
                return 1
        
            cnt = 0
            for v in vowels[k]:
                cnt += helper(v, left - 1)
            
            return cnt % MOD
        
        res = 0
        
        for k in vowels:
            res += helper(k, n-1) % MOD
        
        return res
    