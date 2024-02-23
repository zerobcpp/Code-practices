class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = defaultdict(int)
        N = len(nums)
        for i in nums:
            c[i] += 1
        
        res = []
        
        for i in range(1, N+1):
            if c[i] > 1 or c[i] == 0:
                res.append(i)
            
        return res