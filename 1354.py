class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #matches.sort(key = lambda x: x[1])
        c = defaultdict(list)
        
        for w, l in matches:
            if l not in c:
                c[l].extend([-1, True])
            else:
                c[l][0] -= 1
                c[l][1] = False
        
        #print(c)
        
        for w, l in matches:
            if w not in c:
                c[w].extend([1, True])
            else:
                if c[w][0] > 0:
                    c[w][0] += 1
                    
        
        
        res = [[], []]
        
        for i, v in c.items():
            if v[1] == True and v[0] < 0:
                res[1].append(i)
            elif v[1] == True and v[0] > 0:
                res[0].append(i)
        
        res[0].sort()
        res[1].sort()
        return res
    
    
    def findWinners(self, matches):
        c = {}
        
        for w, l in matches:
            if w not in c:
                c[w] = 0
            if l not in c:
                c[l] = -1
            else:
                c[l] -= 1
        
        res = [[], []]
        for i, v in c.items():
            if v == 0:
                res[0].append(i)
            elif v == -1:
                res[1].append(i)
        
        res[1].sort()
        res[0].sort()
        return res
        
        