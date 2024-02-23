class Solution:
    def longestPalindrome(self, s: str) -> str:
        p1 = p2 = 0
        length = 0
        sol = []
        for add in range (2):
            for i in range (len(s)):
                left = i
                right = i + add
                if left >= 0 and right < len(s):
                    while s[left] == s[right] and left>= 0 and right < len(s):
                        if left - 1 >= 0 and right + 1 < len(s):
                            left -= 1
                            right += 1
                        else:
                            if length < right - left + 1:
                                length = right - left + 1
                                sol = s[left:right + 1]
                            break
                    if length < right - left - 1:
                        length = right - left - 1
                        sol = s[left + 1:right]
                    
        return sol
        
                
                