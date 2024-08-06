class Solution:
    def wordBreak(self, s: str, word: List[str]) -> bool:
        word = set(word)    
        N = len(s)
        cache = {}
        def helper(i):
            if i >= N:
                return True
            if i in cache:
                return cache[i]
            for w in word:
                length = len(w)
                #print(s[i:i+length])
                if s[i:i+length] == w:
                    if helper(i+length):
                        cache[i] = True
                        return True
            cache[i] = False
            return False
        
        helper(0)
        print(len(cache), len(s))
        return cache[0]
    
    def wordBreak(self, s: str, word: List[str]) -> bool:
        word = set(word)    
        N = len(s)
        cache = [None] * (N)
        def helper(i):
            if i >= N:
                return True
            if cache[i] != None:
                return cache[i]
            for w in word:
                length = len(w)
                #print(s[i:i+length])
                if s[i:i+length] == w:
                    if helper(i+length):
                        cache[i] = True
                        return cache[i]
            cache[i] = False
            return cache[i]
        
        helper(0)
        #print(len(cache), len(s))
        return cache[0]
        
        
                