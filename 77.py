class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        combination = set()

        for i in range(k):
            for j in range(1, n ):
                for z in range(n, 1, -1):
                    if j == z:
                        break
                    combination.add((j, z))

        return combination
    