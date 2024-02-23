class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        g = len(goal)
        if n != g:
            return False
        
        if s == goal:
            c = Counter(s)
            for i in c:
                if c[i] == 2:
                    return True
            return False
        
        diff = 0
        for i in range(n):
            if s[i] != goal[i]:
                diff += 1
        
        return diff == 2
        