class Solution:
    def largestVariance(self, s: str) -> int:
        res = 0
        c = Counter(s)
        N = len(s)
        
        def helper(s, cur):
            c = Counter(s)
            diff = 0
            for i in c:
                if i == cur:
                    continue
                diff = max(c[cur] - c[i], diff)
            
            return diff
            
        res = 0    
        for i in range(N):
            temp = []
            for j in range(i, N):
                temp.append(s[j])
                res = max(res,helper(temp, s[j]))
        
        return res
        
                