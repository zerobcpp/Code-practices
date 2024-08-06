class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = {}
        mx = 0
        for i in arr:
            c[i] = c.get(i, 0) + 1
            mx = max(mx, i)
            
        for i in range(mx, -1, -1):
            if i in c and c[i] == i:
                return i
        
        return -1
        