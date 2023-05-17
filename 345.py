# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)
        print(string)
        l = 0
        r = len(string) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while l < r:
            if string[l] in vowels:
                while r > l:
                    if string[r] in vowels:
                        break
                    r -= 1
                string[l], string[r] = string[r], string[l]
                r -= 1
            l += 1
        
        return ''.join(string)