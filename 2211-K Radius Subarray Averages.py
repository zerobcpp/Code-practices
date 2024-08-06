class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k >= n:
            return [-1] * n
        if k == 0:
            return nums
            
        #print(n)
        avg = 2 * k
        res = [-1] * n
        val = 0
        for i in range(k+1):
            val += nums[i]
        if i - avg >= 0:
            res[i-k] = (val//(avg+1))
        
        l = 0
        for j in range(i+1, n):
            val += nums[j]
            
            if j - avg >= 0:
                #print(j, val)
                res[j-k] = (val//(avg+1))
                val -= nums[l]
                l += 1
            
        
        return res
            
            
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        avg = 2 * k + 1
        if k == 0:
            return nums
        if avg > n:
            return res

        s = sum(nums[:avg])
        res[k] = s // avg
        #print(s)
        for i in range(avg, n):
            s -= nums[i - avg]
            s += nums[i]
            res[i-k] = s // avg
        
        return res