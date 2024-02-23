class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        loop = True
        sec = 0
        i = 0
        while tickets[k] > 0:
            i %= len(tickets)
            if tickets[i] > 0:
                tickets[i] -= 1
                sec += 1
            i += 1
        
        return sec