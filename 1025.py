class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #  1 day = 2.0 perday, <= 3 days = 1
        #  7 days = 1.0 per day, >= 4 days = 7
        #  30 days = 0.5 per day >= 8 days = 30
        s30 = deque()
        s7 = deque()
        s = deque()
        res = 0
        for day in days:
            while s and s[0][0] + 1 <= day:
                s.popleft()
            while s7 and s7[0][0] + 7 <= day:
                s7.popleft()
            while s30 and s30[0][0] + 30 <= day:
                s30.popleft()
            s.append((day, res + costs[0]))
            s7.append((day, res + costs[1]))
            s30.append((day, res + costs[2]))
            res = min(s[0][1], s7[0][1], s30[0][1])
            print(s)
            print(s7)
            print(s30)
            print()
        
        return res