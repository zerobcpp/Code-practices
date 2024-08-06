class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        res = 0
        mx = nums[0]
        c = {}
        for i in nums:
            if i not in c:
                c[i] = 1
            else:
                found = False
                for j in range(i, i+mx+1):
                    if j not in c:
                        c[j] = 1
                        found = True
                    if found:
                        break
                    res += 1
        return res
        

    def minIncrementForUnique(self, nums: List[int]) -> int:
        c = defaultdict(int)
        mx = 0
        res = 0
        n = len(nums)
        for i in nums:
            c[i] += 1
            mx = max(i, mx)
        
        
        for i in range(mx+n):
            if i not in c or c[i] <= 1:
                continue
            else:
                cnt = c[i]
                c[i] = 1
                c[i+1] += cnt - 1
                res += cnt - 1
                
        #print(c)
        return res
    
        
    def minIncrementForUnique(self, nums):
        nums.sort()
        res = 0
        cur = 0
        for i in nums:
            res += max(cur - i, 0)
            cur = max(cur, i) + 1
        
        return res