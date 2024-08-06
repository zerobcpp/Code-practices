class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        
        def check(l, w, h, m):
            bulk = False
            heavy = False
            if l >= 10 ** 4 or w >= 10**4 or h >= 10**4 or l * w * h >= 10**9:
                bulk = True
            if m >= 100:
                heavy = True
            
            if bulk and heavy:
                return 'Both'
            elif bulk: 
                return 'Bulky'
            elif heavy:
                return 'Heavy'
            return 'Neither'
        
        return check(length, width, height, mass)