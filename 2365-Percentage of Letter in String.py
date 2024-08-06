class Solution:
    def percentageLetter1(self, s: str, letter: str) -> int:
        n = len(s)
        target = s.count(letter)
        
        return floor((target / n) * 100)
                
    
    def percentageLetter(self, s, letter):
        cnt = 0
        for i in s:
            if letter == i:
                cnt += 1
        
        n = len(s)
        return floor(cnt/n*100)