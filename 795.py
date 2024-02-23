class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def helper(n, k, cur):
            if n == 1:
                return cur
            node = 2 ** (n-1)
            mid = node // 2
            
            if k > mid:
                n_cur = 1 if cur == 0 else 0
                return helper(n-1, k - mid, n_cur)
            else:
                n_cur = 0 if cur == 0 else 1
                return helper(n-1, k, n_cur)
        
        return helper(n, k, 0)

        
        
        
# 0
# 0 1
# 0 1 1 0
# 0 1 1 0 1 0 0 1