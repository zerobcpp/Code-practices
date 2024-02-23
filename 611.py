class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n-2):
            k = i + 2
            if nums[i] == 0:
                continue
            for j in range(i+1, n-1):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                #print(k, j)
                count += k - j - 1
        
        return count