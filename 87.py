class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        N = len(s1)
        N2 = len(s2)
        if N != N2 or Counter(s1) != Counter(s2):
            return False

        cache = {}
        def helper(x, y):
            print(x, y)
            if x == y:
                return True
            if Counter(x) != Counter(y):
                return False
            N = len(x)
            for i in range(1, N):
                if helper(x[:i], y[-i:]) and helper(x[i:], y[:-i]) \
                or helper(x[i:], y[i:]) and helper(x[:i], y[:i]):
                    return True
            return False
        
        return helper(s1, s2)
#func(s1[:i], s2[-i:]) and func(s1[i:], s2[:-i]) or func(s1[:i], s2[:i]) and func(s1[i:], s2[i:]):