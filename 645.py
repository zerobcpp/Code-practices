class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = defaultdict(int)
        N = len(nums)
        for i in nums:
            c[i] += 1
        
        two = []
        zr = []
        
        for i in range(1, N+1):
            if c[i] > 1:
                two.append(i)
            if c[i] == 0:
                zr.append(i)
            
        return two + zr