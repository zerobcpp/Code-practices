class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
    
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        n, m = max(arr), max(target)
        tarr = [0] * (m+1)
        sarr = [0] * (n+1)
        
        for i in target:
            tarr[i] += 1
        
        for i in arr:
            sarr[i] += 1
        
        return sarr == tarr
    
    
    def canBeEqual(self, target, arr):
        c = defaultdict(int)
        for i in arr:
            c[i] += 1
        
        for i in target:
            c[i] -= 1
            if c[i] < 0:
                return False
        
        return True
            