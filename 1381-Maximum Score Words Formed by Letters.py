class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        c = Counter(letters)
        
        N = len(words)
        self.res = 0
        def helper(i, s): 
            if i >= N:
                self.res = max(self.res, s)
                return
            
            helper(i+1, s)
            
            for j in range(i, N):
                t = 0
                can = True
                wc = Counter(words[j])
                for k, v in wc.items():
                    if k not in c or c[k] < v:
                        can = False
                        break
                if can:
                    tot = 0
                    for k,v in wc.items():
                        c[k] -= v
                        tot += score[ord(k) - ord('a')] * v

                    helper(j+1, s + tot)

                    for k,v in wc.items():
                        c[k] += v
            
            return
        
        for i in range(N):
            helper(i, 0)
        
        return self.res
            
            
            