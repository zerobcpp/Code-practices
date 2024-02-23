class Solution:
    def checkStraightLine(self, cord: List[List[int]]) -> bool:
        def slope(y2, y1, x2, x1):
            return (y2 - y1)/(x2 - x1)
        
        x, dx, y, dy = cord[0][0], cord[0][1], cord[1][0], cord[1][1]
        mx = atan2(dy - y, dx - x)
        n = len(cord)
        for i in range(2, n):
            x, dx, y, dy = cord[i-1][0], cord[i][1], cord[i-1][0], cord[i][1]
            
            check = atan2(dy - y, dx - x)
            if check != mx:
                return False
        
        return True