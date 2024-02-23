import heapq
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = [-1] * numOnes
        res.extend([0] * numZeros)
        res.extend([1] * numNegOnes)
        heapq.heapify(res)
        
        count = 0
        while k:
            count += -heappop(res)
            k -= 1
        
        return count