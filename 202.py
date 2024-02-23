class Solution:
    def isHappy(self, n: int) -> bool:
        c = set()
        s = list(str(n))
        res = 0
        while res != 1:
            if res % 1 != 0 and res in c:
                return False
            c.add(res)
            res = sum([int(i) ** 2 for i in s])
            s = list(str(res))
        return True