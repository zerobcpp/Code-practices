class Solution:
    def strangePrinter(self, s: str) -> int:
        cache = {}
        s = re.sub(r'(.)\1*', r'\1', s)
        N = len(s)
        
        def helper(l, r):
            if l >= N or r < 0:
                return float('inf')
            if (l, r) in cache:
                return cache[l, r]
            count = float('inf')
            prev = -1
            for i in range(l, r):
                if s[i] != s[r] and prev == -1:
                    prev = i
                if prev != -1:
                    count = min(count, 1 + helper(i+1, r) + helper(prev, i))
            
            if prev == -1:
                count = 0
            #print(count)
            cache[l, r] = count
            return cache[l, r]
        
        return helper(0, N-1) + 1