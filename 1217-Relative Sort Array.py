class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        nia = []
        c = {}
        for i, v in enumerate(arr2):
            c[v] = i
        
        for i in arr1:
            if i not in c:
                nia.append(i)
            else:
                res.append(i)
        
        res.sort(key=lambda x: c[x])
        nia.sort()
        res += nia
        return res
        
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mx = max(arr1)
        c = defaultdict(int)
        n = len(arr1)
            
        for i in arr1:
            c[i] += 1
        
        res = []
        for i in arr2:
            while c[i]:
                res.append(i)
                c[i] -= 1
        
        for i in range(mx+1):
            if i in c:
                while c[i]:
                    res.append(i)
                    c[i] -= 1
        
        return res
            
            
        
        

        
        
        