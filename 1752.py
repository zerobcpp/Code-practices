class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for left, right in zip(l, r):
            
            temp = sorted(nums[left:right+1])
            t = True
            c = temp[1] - temp[0]
            N = len(temp)
            
            for i in range(N-1, 0, -1):
                if temp[i] - temp[i-1] != c:
                    #print(temp[i], temp[i-1])
                    t = False
                    break
            
            res.append(t)
        
        return res
                