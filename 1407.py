class Solution:
    def groupThePeople(self, group: List[int]) -> List[List[int]]:
        n = len(group)
        c = defaultdict(list)
        
        for i, v in enumerate(group):
            c[v].append(i)
        
        res = []
        
        for s, v in c.items():
            
            while c[s]:
                temp = []
                while len(temp) < s:
                    temp.append(c[s].pop())
                res.append(temp)
        
        return res[::-1]
        
        