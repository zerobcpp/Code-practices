class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        st = []
        for i in range(len(arr)):
            heapq.heappush(st, ((arr[i] / arr[-1]), i, len(arr) - 1))
            
        while st and k > 1:
            
            fact, i, j = heappop(st)
            j -= 1
            k -= 1      
            
            if j > i:
                heappush(st, (arr[i]/arr[j],i, j))
            
            #print(st)
            
        fact, i, j = heappop(st)
        return [arr[i], arr[j]]
        

            
