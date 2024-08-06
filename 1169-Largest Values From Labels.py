class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        st = [(-v, l) for v, l in zip(values, labels)]
        #print(st)
        heapify(st)
        res = 0
        c = defaultdict(int)
        while st and numWanted > 0:
            val, lab = heappop(st)
            if c[lab] < useLimit:
                res -= val
                c[lab] += 1
                numWanted -= 1
            
        #print(c)
        return res