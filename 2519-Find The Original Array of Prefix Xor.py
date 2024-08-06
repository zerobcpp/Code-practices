class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        N = len(pref)
        res.append(pref[0])
        for i in range(1, N):
            res.append(pref[i-1] ^ pref[i])
            
        
        #print(res)
        return res