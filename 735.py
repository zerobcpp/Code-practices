class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        c = []
        res = []
        for i in asteroids:
            broke = False
            while c and ((c[-1] > 0 and i < 0) or (c[-1] < 0 and i > 0)):
                if (c[-1] > 0 and i < 0):
                    if (c[-1] == -i or c[-1] < -i) and not broke:
                        c.pop()
                    else:
                        broke = True
                        res.append(c.pop())
                    
                elif (c[-1] < 0 and i > 0):
                    if (-c[-1] == i or -c[-1] < i) and not broke:
                        c.pop()
                    else:
                        broke = True
                        res.append(max(-c.pop(), i))
                
            c.append(i)
        
        return res[::-1]