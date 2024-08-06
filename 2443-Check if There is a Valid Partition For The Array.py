class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        cache = [-1] * N
        def helper(i):
            print(i, end = ' ')
            if i >= N:
                return True
            if cache[i] != -1:
                return cache[i]
            
            if i + 1 < N and nums[i] == nums[i+1]:
                if helper(i+2):
                    cache[i] = True
                    return True
            if i + 2 < N and nums[i] == nums[i+2] and nums[i] == nums[i+1]:
                if helper(i+3):
                    cache[i] = True
                    return True
            if i + 2 < N and nums[i] == nums[i+1] - 1 and nums[i] == nums[i+2] - 2:
                if helper(i+3):
                    cache[i] = True
                    return True
                
            #print('\n')
            cache[i] = False
            return False
        helper(0)
        print(cache)
        return cache[0]