class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        n = len(s)
        
        for i in range(n):
            for dx in range(2):
                left = i
                right = i + dx
                
                while left >= 0 and right < n and s[left] == s[right]:
                    #print(left, right)
                    if len(res) < right - left + 1:
                        res = s[left:right+1]
                    left -= 1
                    right += 1
                    
        
        return res