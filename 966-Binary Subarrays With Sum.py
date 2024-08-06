class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sm = 0 
        c = defaultdict(int)
        res = 0
        for i in nums:
            sm += i
            if sm == goal:
                res += 1
            
            res += c[sm - goal]
            c[sm] += 1
        
        print(c)
        
        return res