class Solution:
    def wordBreak(self, s: str, word: List[str]) -> bool:
        word = set(word)
        N = len(max(word, key = len))
        
        cache = {}
        def helper(i):
            if i >= N:
                return True
            
            for w in word:
                length = len(w)
            #    print(s[i:length])
                if s[i:length] == w:
                    if helper(i+length):
                        return True
            
            return False
        
        return helper(0)
                