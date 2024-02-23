# 2024. Maximize the Confusion of an Exam

class Solution:
    def maxConsecutiveAnswers(self, aKey: str, k: int) -> int:
        res = 0
        l = 0
        N = len(aKey)
        #c = {'T' : 0, 'F' : 0}
        c = defaultdict(int)
        for r in range(N):
            idx = aKey[r]
            c[idx] += 1
            
            while min(c['T'], c['F']) > k:
                idx = aKey[l]
                c[idx] -= 1
                l += 1
                
            res = max(res, r - l + 1)
        
        
        
        return res 
            