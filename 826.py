class Solution:
    def soupServings(self, n: int) -> float:
        cache = {}
        def helper(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            if (a, b) in cache:
                 return cache[a, b]
            p1 = helper(a-100, b-0)
            p2 = helper(a-75, b-25)
            p3 = helper(a-50, b-50)
            p4 = helper(a-25, b-75)
            cache[a,b] = (p1 + p2 + p3 + p4) / 4
            #print(cache[a,b])
            return cache[a, b]
        
        for i in range(1, n, 25):
            if helper(i, i) > 1.0 - 10 ** -5:
                return 1
        return helper(n, n)