# 347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        for i in nums:
            c[i] = c.get(i, 0) + 1
        
        temp = sorted(c.items(), key = lambda x: x[1], reverse = True)
        print(temp)
        res = []
        for i in range(k):
            res.append(temp[i][0])
        
        return res
    
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        return [i for i, v in c.most_common(k)]
    
    def topKFrequent(self, nums, k):
        c = {}
        for i in nums:
            c[i] = c.get(i, 0) + 1
        
        heap = []
        for i, v in c.items():
            heapq.heappush(heap, (-v, i))
        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
    
    def topKFrequent(self, nums, k):
        n = len(nums)
        c = Counter(nums)
        buckets = [[] for _ in range(n+1)]
        
        for i, v in c.items():
            buckets[v].append(i)
        
        res = []
        for i in range(n, -1, -1):
            if buckets[i]:
                res.extend(buckets[i])
        
        return res[:k]
    
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        idx = list(c.keys())
        n = len(idx)
        res = []
        temp = k
        k = n - k
        def helper(l, r):
            pidx, p = randint(l, r), l
            pivot = c[idx[pidx]]
            idx[r], idx[pidx] = idx[pidx], idx[r]
            for i in range(l, r):
                if c[idx[i]] < pivot:
                    idx[p], idx[i] = idx[i], idx[p]
                    p += 1
            idx[r], idx[p] = idx[p], idx[r]
            
            if p > k:
                return helper(l, p-1)
            elif p < k:
                return helper(p+1, r)
            else:
                return
        
        helper(0, n-1)
        return idx[::-1][:temp]


    def topKFrequent(self, nums, k):
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

