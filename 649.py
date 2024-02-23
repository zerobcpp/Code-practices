class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = []
        d = []
        for i, v in enumerate(senate):
            if v == 'R':
                r.append(i)
            else:
                d.append(i)
        
        while r and d:
            ridx = r.pop()
            didx = d.pop()
            
            if ridx < didx:
                r.append(ridx + 1)
            else:
                d.append(didx + 1)
        
        return 'Radiant' if r else 'Dire'
            