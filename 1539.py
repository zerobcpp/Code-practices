class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        N = len(nums)
        c = defaultdict(list)
        mx = 0
        for i in range(N-1, -1, -1):
            for j in range(len(nums[i])):
                dia = i + j
                c[dia].append(nums[i][j])
                mx = max(mx, dia)
        
        res = []
        
        for i in range(mx+1):
            
            res.extend(c[i])
        
        return res
                