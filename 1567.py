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