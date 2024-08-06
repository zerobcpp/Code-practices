class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        turn = time // (n-1)
        position = time % (n-1)
        #print(turn, position)
        
        return n - position if turn % 2 != 0 else position + 1
        
        
    
    
    def passThePillow(self, n, time):
        dirs = 1
        position = 1
        while time:
            position += dirs
            if position == 1 or position == n:
                dirs *= -1
            
            time -= 1
            
        
        return position