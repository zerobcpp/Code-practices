class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        arr = []
        def helper(start):
            if len(arr) == k:
                res.append(arr[:])
            for i in range(start, n+1):
                arr.append(i)
                helper(i+1)
                arr.pop()
        
        helper(1)
        
        return res
            