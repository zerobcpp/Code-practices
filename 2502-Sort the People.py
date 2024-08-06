class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        c = list(zip(heights, names))
        c.sort(reverse = True)
        return [i[1] for i in c]

    
    
    def sortPeople(self, names, heights):
        mx = max(heights)
        c = defaultdict(list)
        
        for h, n in zip(heights, names):
            c[h].append(n)
        
        #print(c)
        res = []
        for i in range(mx, -1, -1):
            if c[i]:
                res.extend(c[i])
        
        return res
    
    def sortPeople(self, names, heights):
        c = [[-height, name] for name, height in zip(names, heights)]
        heapify(c)
        res = []
        while c:
            height, name = heappop(c)
            res.append(name)
        
        return res