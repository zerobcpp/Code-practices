class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        self.res = N = len(s)
        
        def helper(i):
        
            for w in words:
                length = len(w)
                if s[i:i+length] == w:
                    self.res -= length
        
        for i in range(N):
            helper(i)
        
        return self.res