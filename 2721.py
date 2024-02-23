class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        c = defaultdict(list)
        
        for i, v in enumerate(nums):
            c[v].append(i)
        
        res = []
        n = len(nums)
        for i in range(n):
            temp = 0
            for idx in c[nums[i]]:
                temp += abs(i - idx)
                #print(idx, i, temp)
            
            res.append(temp)
        
        return res