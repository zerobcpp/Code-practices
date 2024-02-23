class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        target = s.count(letter)
        
        return floor((target / n) * 100)
                
            