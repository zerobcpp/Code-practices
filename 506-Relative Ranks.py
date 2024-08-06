class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        lst = []
        
        for i, v in enumerate(score):
            lst.append([v, i])
        
        lst.sort()
        #print(lst)
        res = [0] * len(score)
        cnt = 0
        while lst:
            s, r = lst.pop()
            if cnt == 0:
                res[r] = ('Gold Medal')
            elif cnt == 1:
                res[r] = ('Silver Medal')
            elif cnt == 2:
                res[r] = ('Bronze Medal')
            else:
                res[r] = str(cnt+1)
            
            cnt += 1
        
        return res


                