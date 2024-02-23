class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = set(s)
        
        for i in t:
            if i not in c:
                return i
        
        return -1