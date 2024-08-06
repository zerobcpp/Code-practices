class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        return max(c.keys(), key = c.get)
    
    
    def majorityElement(self, nums):
        c = defaultdict(int)
        mx = 0
        res = None
        for i in nums: 
            c[i] += 1
            if c[i] > mx:
                mx = c[i]
                res = i
        
        return res
    
    def majorityElement(self, nums):
        cand = None
        cnt = 0
        
        for i in nums:
            if cand == None or cnt == 0:
                cand = i
            if i == cand:
                cnt += 1
            else:
                cnt -= 1
        
        return cand