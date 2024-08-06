class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r = deque()
        d = deque()
        for i, v in enumerate(senate):
            if v == 'R':
                r.append(i)
            else:
                d.append(i)
        
        while r and d:
            ridx = r.popleft()
            didx = d.popleft()
            
            if ridx < didx:
                r.append(ridx + n)
            else:
                d.append(didx + n)
        
        return 'Radiant' if r else 'Dire'
            