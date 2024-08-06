class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        g = len(goal)
        if n != g:
            return False
        
        if s == goal:
            c = Counter(s)
            for i in c:
                if c[i] >= 2:
                    return True
            return False
        
        a,b = -1, -1
        for i in range(n):
            if s[i] != goal[i]:
                if a == -1:
                    a = i
                elif b == -1:
                    b = i
                else:
                    return False
    
        return s[a] == goal[b] and s[b] == goal[a]
        
        
        