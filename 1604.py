class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = defaultdict(int)
        for i in arr:
            c[i] += 1
        
        data = defaultdict(list)
        
        for i, v in c.items():
            data[v].append(i)
        
        mx = max(data.keys())
        unique = len(c)
        
        for i in range(1, mx + 1):
            if i in data:
                for num in data[i]:
                    if k - i >= 0:
                        k -= i
                        unique -= 1
        
        return unique
    
    # [4,3,1,1,3,3,2]
    # [1,1,2,3,3,3,4]