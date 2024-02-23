class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        n = len(s)
        c = defaultdict(int)
        vowel = ['a', 'e', 'i', 'o', 'u']
        cnt = 0
        res = 0
        for r in range(n):
            idx = s[r]
            c[idx] += 1
            if idx in vowel:
                cnt += 1
            
            while sum(c.values()) > k:
                idx = s[l]
                c[idx] -= 1
                if idx in vowel:
                    cnt -= 1
                l += 1
            #print(c)
            res = max(res, cnt)
        
        return res
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        count = 0
        for i in range(k):
            if s[i] in vowel:
                count += 1
        
        res = count
        
        for i in range(k, n):
            count += 1 if s[i] in vowel else 0
            count -= 1 if s[i-k] in vowel else 0
            res = max(res, count)
        
        return res