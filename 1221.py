class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        target = n // 4
        cand = None
        cnt = 0
        for i in arr: 
            if cnt == 0:
                cand = i
            if cand == i:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt >= target: 
                return i
        
        return -1