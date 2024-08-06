class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        s = set()
        
        for i, v in c.items():
            if v in s:
                return False
            s.add(v)
        
        return True
    
    
    def uniqueOccurrences(self, arr):
        c = Counter(arr)
        s = set(list(c.values()))
        
        
        
        return len(s) == len(c)