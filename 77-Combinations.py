class Solution:
    def combine(self, n: int, k: int):
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
    
    def combine2(self, arr, k):
        res = []
        n = len(arr)
        path = []
        def backtrack(i):
            if len(path) >= k:
                res.append(path[:])
                return
            for j in range(i, n):
                path.append(arr[j])
                backtrack(j+1)
                path.pop()
            
            return
        backtrack(0)
        return res
    

if __name__ == "__main__":
    s = Solution()
    #print(s.combine(4, 2))
    print(s.combine2([4, 5, 6, 10], 3))
    