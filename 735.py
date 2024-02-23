class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for i in asteroids:
            res.append(i)
            while len(res) >=2 and res[-2] > 0 and res[-1] < 0:
                x, y = res.pop(), res.pop()
                if -x != y:
                    if -x > y:
                        res.append(x)
                    else:
                        res.append(y)
                #print(res)
        
        return res
    
    
