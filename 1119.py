class Solution:
    def isRobotBounded(self, instrs: str) -> bool:
        dirs = 0
        points = [0, 0]
        movement = {
            0 : (1, 0),
            90 : (0, 1),
            180 : (-1, 0),
            270 : (0, -1)
        }
        for inst in instrs:
            
            if inst == 'L':
                dirs += 90
            elif inst == 'R':
                dirs -= 90
            else:
                move = movement[dirs]
                points[0] += move[0]
                points[1] += move[1]
            
            dirs %= 360
            #print(points, dirs)
        
        return all(i == 0 for i in points) or dirs != 0
            
                
            
            