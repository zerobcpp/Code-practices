class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        happy = 0
        can_make_happy = 0
        max_can_make_happy = 0
        for i in range(len(customers)):
            if i >= minutes and grumpy[i - minutes] == 1:
                can_make_happy -= customers[i - minutes]
            if grumpy[i] == 1:
                can_make_happy += customers[i]
            else:
                happy += customers[i]
            max_can_make_happy = max(max_can_make_happy, can_make_happy)
        return happy + max_can_make_happy
        
        
        
"""
 [1,0,1,2,1,1,7,5]
 [0,1,0,1,0,1,0,1]
 """