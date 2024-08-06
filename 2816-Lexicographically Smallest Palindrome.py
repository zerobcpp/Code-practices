class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] != s[r]:
                s[l] = min(s[l], s[r])
                s[r] = s[l]
            l += 1
            r -= 1
        
        return ''.join(s)