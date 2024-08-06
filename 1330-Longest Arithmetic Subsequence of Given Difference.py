class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = 0
        N = len(arr)
        c = defaultdict(int)
        
        for i in arr:
            diff = i - difference
            c[i] = c[diff] + 1
            res = max(c[i], res )
        print(c)
        return res