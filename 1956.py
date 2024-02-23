class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        N = len(arr)
        res = 0 
        for i in range(1, N):
            if arr[i] >= res + 1:
                res += 1
        
        return res