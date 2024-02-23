class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        
        res = 0
        for i in range(N):
            res = max(res, len(arr[i]))
            for j in range(i+1, N):
                res = max(res, len(arr[i])  + len(arr[j]))
        
        return res