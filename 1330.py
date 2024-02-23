class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        self.res = 0
        N = len(arr)
        @cache
        def helper(i, prev):
            if i >= N:
                return 0
            
            nc = helper(i+1, prev)
            count = 0
            if prev + difference == arr[i] or prev == -float('inf'):
                count = max(1 + helper(i+1, arr[i]), helper(i+1, prev))
            
            
            return max(nc,count)
        
        return helper(0, -float('inf'))