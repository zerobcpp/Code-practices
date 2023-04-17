# 347. Top K Frequent Elements
class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        c = Counter(nums)
        return [i for i, _ in c.most_common(k)]

    def topKFrequent2(self, nums, k):
        n = len(nums)
        c = Counter(nums)
        buckets = [[] for _ in range(n + 1)]

        res = []
        for i, v in c.items():
            buckets[v].append(i)

        for i in range(n, -1, -1):
            if k <= 0:
                break
            if buckets[i]:
                res.extend(buckets[i])
                k -= len(buckets[i])

        return res

    def topKFrequent(self, nums, k):
        heap = []
        c = Counter(nums)

        for i, v in c.items():
            heapq.heappush(heap, [-v, i])

        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1

        return res