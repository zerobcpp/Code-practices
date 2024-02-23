class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        self.res = 0
        
        def helper(i, strs):
            self.res = max(self.res, len(strs))
            #print(strs)
            if i >= N:
                return
            
            for i in range(i, N):
                unique = True
                count = set()
                for char in arr[i]:
                    if char in count or char in strs:
                        unique = False
                        break
                    count.add(char)
                
                if unique:
                    count.update(strs)
                    helper(i+1, count)
                else:
                    helper(i+1, strs)
                
            return
        
        helper(0, set())
        return self.res
    