class Solution:
    def maxValueOfCoins1(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        cache = {}

        def helper(idx, n):
            if idx == 0:
                return 0
            if (idx, n) in cache:
                return cache[idx, n]
            cache[idx, n] = 0
            x = 0
            for i in range(min(n, len(piles[idx - 1])) + 1):
                if i > 0:
                    x += piles[idx - 1][i - 1]

                cache[idx, n] = max(cache[idx, n], helper(idx - 1, n - i) + x)

            return cache[idx, n]

        return helper(n, k)

    def maxValueOfCoins(self, piles, k):
        n = len(piles)
        cache = {}

        def helper(i, c):
            # print(cache)
            if i >= n or c <= 0:
                return 0
            if (i, c) in cache:
                return cache[i, c]

            cache[i, c] = 0
            x = 0
            for j in range(min(c, len(piles[i])) + 1):
                if j > 0:
                    x += piles[i][j - 1]
                cache[i, c] = max(cache[i, c], helper(i + 1, c - j) + x)

            return cache[i, c]

        helper(0, k)
        return cache[0, k]


