class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split()
        return len(s[-1])
    
    
    def lengthOfLastWord(self, s):
        s = s.split()
        for i in s[::-1]:
            if i != '':
                return len(i)
        
        return -1