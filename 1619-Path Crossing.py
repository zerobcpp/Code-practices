class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        x = y = 0
        seen.add((x,y))
        dirs = 'NESW'
        for i in path:
            if i == dirs[0]:
                y += 1
            elif i == dirs[1]:
                x += 1
            elif i == dirs[2]:
                y -= 1
            else:
                x -= 1
            if (x, y) in seen:
                return True
            
            seen.add((x,y))
        
        return False
        
        