# 451. Sort Characters By Frequency
class Solution:
    def frequencySort1(self, s: str) -> str:
        c = Counter(s)
        count = max(c.values())
        buckets = [[] for i in range(count + 1)]
        for i, v in c.items():
            buckets[v].append(i)
        print(buckets)
        res = []
        for i in range(count, -1, -1):
            for c in buckets[i]:
                res.extend(c * i)

        return res

    def frequencySort2(self, s):
        c = Counter(s)
        c = sorted(c.items(), key=lambda x: x[1], reverse=True)
        print(c)
        res = []
        for i, v in c:
            res.extend(i * v)

        return res

    def frequencySort(self, s):
        # python older version
        c = Counter(s)
        c = sorted(c.items(), key=operator.itemgetter(1))

        return ''.join([v * i for i, v in c[::-1]])