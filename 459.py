class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n):
            temp = s[:i]
            if not temp:
                mul = 1
            else:
                mul = n // len(temp)
            
            if temp * mul == s:
                return True
        
        return False
    
    
    def repeatedSubstringPattern(self, s):
        temp = s * 2
        
        return s in temp