class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sst = []
        tst = []

        for i in s:
            if i == '#':
                if sst:
                    sst.pop()
            else:
                sst.append(i)

        for i in t:
            if i == '#':
                if tst:
                    tst.pop()
            else:
                tst.append(i)

        return tst == sst