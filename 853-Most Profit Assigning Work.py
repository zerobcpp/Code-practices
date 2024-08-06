class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        res = 0
        c = []
        c += [[0, 0]]
        for d, p in zip(difficulty, profit):
            c.append([d, p])
        c.sort()
        n = len(c)
        for i in range(1, n):
            c[i][1] = max(c[i][1], c[i-1][1])
        
        #print(c, n)
            
        for i in worker:
            idx = bisect_left(c, [i, ])
            while idx >= n:
                idx -= 1
            #print(i, idx, end = ' ')
            while idx > 0 and i < c[idx][0]:
                idx -= 1
            while idx + 1 < n and c[idx+1][0] == i:
                idx += 1
            #print(idx, end = ' ')
            res += c[idx][1]
            #print(res, idx)
        
        return res
    
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        mx = max(worker)
        bucket = [0] * (mx+1)
        c = {}
        
        for d, p in zip(difficulty, profit):
            c[d] = max(c.get(d, 0), p)
        
        
        for i in range(1, mx+1):
            bucket[i] = max(bucket[i-1], c.get(i, 0))
        
        res = 0
        for i in worker:
            res += bucket[i]
        
        return res
        