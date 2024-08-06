class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs = Counter(s)
        ct = Counter(t)
        
        for i, v in ct.items():
            if v != cs[i]:
                return i
        return -1
    
    
    def findTheDifference(self, s, t):
        res = 0
        
        for i in s:
            res ^= ord(i)
        for i in t:
            res ^= ord(i)
        
        return chr(res)