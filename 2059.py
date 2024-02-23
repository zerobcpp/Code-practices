class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        N = len(s)
        
        ms = {i:[-1, -1] for i in s}
        
        for i in range(N):
            k = s[i]
            if ms[k][0] == -1:
                ms[k][0] = i
            ms[k][1] = i
        
        res = 0
        print(ms)
        for k, length in ms.items():
            left, right = length
            temp = set()
            for i in range(left+1, right):
                temp.add(s[i])
            
            #print(temp)
            res += len(temp)
        
        return res