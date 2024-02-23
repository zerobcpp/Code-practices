class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        res = []
        
        two = -float('inf')
        for i in nums:
            
            if i < two:
                return True
            while res and res[-1] < i:
                two = res.pop()
            
            res.append(i)
            #print(res, two)
            
        
        return False