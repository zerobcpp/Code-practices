class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        N = len(s)
        vowels = 0
        for i in range(N//2):
            #print(s[i])
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowels += 1
        
        for i in range(N//2, N):
            #print(s[i])
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowels -= 1
        #print(vowels)
        return vowels == 0
        
            