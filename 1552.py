class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        res = []
        N = len(target)
        idx = 0
        i = 1
        insert = True
        while ans != target and i < n+1:
            ans.append(i)
            res.append('Push')
            insert = True
            if ans and ans[-1] != target[idx] :
                ans.pop()
                res.append('Pop')
                insert = False
            
            if insert:
                idx += 1
            i += 1
            #print(ans, res)


        
        #print(ans, res)
        return res
            
            

                
        
        