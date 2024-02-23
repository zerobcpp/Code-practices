class Solution:
    def reorganizeString(self, s: str) -> str:
        c = {}
        for i in s:
            c[i] = c.get(i, 0) + 1
        
        count = [[v, i] for i, v in c.items()]
        count.sort(reverse = True)
        n = len(count)
        res = []
        
        while count:
            #print(count)
            most = count[0][1]
            count[0][0] -= 1
            least = None
            if len(count) != 1:
                least = count[-1][1]
                count[-1][0] -= 1
                
            if least:
                res.extend([most, least])
            else:
                res.append(most)
            
            while count and count[-1][0] == 0:
                count.pop()
            
            #print(res)
            if res[-1] == res[-2]:
                return ''
        
        return ''.join(res)