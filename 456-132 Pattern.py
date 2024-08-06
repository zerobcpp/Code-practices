class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        res = []
        
        two = -float('inf')
        for i in nums[::-1]:
            
            if i < two and res:
                return True
            while res and res[-1] < i:
                two = res.pop()
            
            res.append(i)
            #print(res, two)
            
        
        return False