class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        e1s, e1e = event1[0].split(':'), event1[1].split(':')
        e2s, e2e = event2[0].split(':'), event2[1].split(':')
        
        e1s = int(e1s[0]) * 60 + int(e1s[1])
        e1e = int(e1e[0]) * 60 + int(e1e[1])
        e2s = int(e2s[0]) * 60 + int(e2s[1])
        e2e = int(e2e[0]) * 60 + int(e2e[1])
        
        print(e1s, e1e, e2s, e2e)
        if e1s <= e2e and e2s <= e1e:
            return 1
        return 0
        
        
