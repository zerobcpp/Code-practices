class Solution:
    def largestVariance(self, s: str) -> int:
        res = 0
        c = Counter(s)
        seen = set()
        res = 0
        for i in s:
            for j in s:
                if i == j:
                    continue
                
                diff = 0
                isJ = False
                jcnt = c[j]
                for k in s:
                    if k != i and k != j:
                        continue
                    if k == i:
                        diff += 1
                    elif k == j:
                        diff -= 1
                        isJ = True
                        jcnt -= 1
                        if diff < 0 and jcnt > 0:
                            diff = 0
                            isJ = False
                    if isJ:
                        res = max(res, diff)

        return res