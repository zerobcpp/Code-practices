class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = []
        c = defaultdict(int)
        last = {}
        
        for i, v in enumerate(s):
            last[v] = i
        
        cnt = 0
        for i in s:

            #print(res, c)
            if c[i] == 0:
                while res and res[-1] > i and last[res[-1]] > cnt:
                    c[res.pop()] -= 1
            
            if c[i] + 1 < 2:
                res.append(i)
                c[i] += 1
            cnt += 1

        #print(res, c)
        
        return ''.join(res)    