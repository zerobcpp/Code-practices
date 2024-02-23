class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        N = len(words)
        
        c = defaultdict(dict)
        for i in range(N):
            temp = {}
            for char in words[i]:
                temp[char] = 1
            
            c[i] = temp
        
        res = 0 
        
        for i in range(N):
            for j in range(i+1, N):
                if c[i] == c[j]:
                    res += 1
        
        return res