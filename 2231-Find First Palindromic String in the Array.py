class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for i in words:
            if i == i[::-1]:
                return i
        
        return ''
    
    
    def firstPalindrome(self, words):
        
        for i in words:
            N = len(i)
            found = True
            for l in range(N):
                r = N - l - 1
                if i[l] != i[r]:
                    found = False
                    break
            
            if found:
                return i
        
        return ''
                