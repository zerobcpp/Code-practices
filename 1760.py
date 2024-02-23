class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        c = defaultdict(list)
        
        for i in pieces:
            c[i[0]] = i
        
        
        res = []
        for i in arr:
            if i in c:
                res.extend(c[i])
        
        #print(res)
        return res == arr