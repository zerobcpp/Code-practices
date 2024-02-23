class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        cache = {N: True}
        def helper(i):
            print(i, end = ' ')
            if i >= N:
                return True
            if i in cache:
                return cache[i]
            cur = False
            if i + 1 < N and nums[i] == nums[i+1]:
                cur = True
                if helper(i+2):
                    return True
            if i + 2 < N and nums[i] == nums[i+2]:
                cur = True
                if helper(i+3):
                    return True
            if i + 2 < N and nums[i] == nums[i+1] + 1 and nums[i] == nums[i+2] + 2:
                cur = True
                if helper(i+2):
                    return True
                
            #print('\n')
            cache[i] = cur
            return cur
        helper(0)
        #print(cache)
        return cache[0]