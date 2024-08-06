class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = defaultdict(int)
        target = len(arr) // 4 + 1
        for i in arr:
            c[i] += 1
        
        
        for i, v in c.items():
            if v >= target:
                return i
        return -1