class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        words = set(wordDict)
        res = []
        arr = []
        def helper(i):
            if i >= N or len(arr) == N:
                res.append(" ".join(arr))
                return
                
            for j in range(i, N):
                cur = s[i:j+1]
                
                if cur in words:
                    arr.append(cur)
                    helper(j+1)
                    arr.pop()
        
        helper(0)
        return res
            
            
            
                
                #7
# "c a t s a n d d o g"
# ["cat","cats","and","sand","dog"]       