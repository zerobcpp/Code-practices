class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        res = []
        def helper(z, o, arr):
            if len(arr) > high:
                return
            if low <= len(arr) <= high and (z >= zero or o >= one):
                res.append(arr[:])
            helper(z+1, o, arr+[0])
            helper(z, o+1, arr+[1])
        
        helper(0, 0, [])
        #print(res, end = '\n')
        return len(res)