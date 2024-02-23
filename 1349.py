class Solution:
    def checkStraightLine(self, cord: List[List[int]]) -> bool:
        def slope(y2, y1, x2, x1):
            if x2 - x1 == 0:
                return float('inf')
            return (y2 - y1)/(x2 - x1)
        
        x, dx, y, dy = cord[0][0], cord[1][0], cord[0][1], cord[1][1]
        mx = slope(dy, y, dx, x)
        n = len(cord)
        for i in range(2, n):
            x, y = cord[i][0], cord[i][1]
            #print(i, end = ':')
            check = slope(dy, y, dx, x)
            if check != mx:
                return False
        
        return True