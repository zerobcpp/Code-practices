class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        arr = []
        res = []
        def helper(i):

            if i >= N:
                res.append(arr[:])
                return
            
            for j in range(i, N):
                left, right = i, j
                p = True
                while left < right:
                    if s[left] != s[right]:
                        p = False
                        break
                    left += 1
                    right -= 1
                
                if p:
                    arr.append((s[i:j+1]))
                    helper(j+1)
                    arr.pop()
        
        helper(0)
        
        return res