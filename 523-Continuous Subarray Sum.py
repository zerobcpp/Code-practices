class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        c = {0:-1}
        sm = 0
        n = len(nums)
        for i in range(n):
            sm += nums[i]
            sm %= k
            if sm in c:
                #print(sm, nums[i], i, c[sm])
                if i - c[sm] > 1:
                    #print(c, sm, i)
                    return True
            else:
                c[sm] = i
            #print(c)
        
        
        return False
        