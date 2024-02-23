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
        
    
    def halvesAreAlike(self, s):
        N = len(s)
        s = s.lower()
        c = set('aeiou')
        vowels = 0
        for i in range(N//2):
            if s[i] in c:
                vowels += 1
        
        for i in range(N//2, N):
            if s[i] in c:
                vowels -= 1
        
        return vowels == 0