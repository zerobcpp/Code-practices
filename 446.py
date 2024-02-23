class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        c = [defaultdict(int) for i in range(N)]
        
        for i in range(N):
            
            for j in range(i):
                diff = nums[i] - nums[j]
                
                ways = c[j].get(diff, 0)
                c[i][diff] += ways + 1
                res += ways
        
        
        print(*c, end = '\n')
        return res
                
                
        
        
        
        
        

# defaultdict(<class 'int'>, {2: 1, 4: 1, 6: 1, 8: 1}) 
# defaultdict(<class 'int'>, {2: 1, 4: 1, 6: 1}) 
# defaultdict(<class 'int'>, {2: 1, 4: 1}) 
# defaultdict(<class 'int'>, {2: 1}) 
# defaultdict(<class 'int'>, {})
