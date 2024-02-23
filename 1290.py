class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        N = len(arr1)
        M = len(arr2)
        arr2.sort()
        @cache
        def helper(i, prev):
            if i >= N:
                return 0
            
            ways = float('inf')
            if arr1[i] > prev:
                ways = helper(i+1, arr1[i])
            
            idx = bisect_right(arr2, prev)
            if idx < M:
                return min(ways, 1 + helper(i+1, arr2[idx]))
            
            return ways
        
        return helper(0,-1)