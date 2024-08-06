class Solution:
    def reverseVowels(self, s):
        l, r = 0, len(s) - 1
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        string = [i for i in s]
        
        while l < r:
            #print(l, r)
            if string[l] in vowels:
                while r > l:
                    if string[r] in vowels:
                        break
                    r -= 1
                string[l], string[r] = string[r], string[l]
                r -= 1
            l += 1
        
        return "".join(string)
    