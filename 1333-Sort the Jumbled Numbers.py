class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        numsToVal = {}
        numsToIdx = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            cur = []
            temp = nums[i]
            calculated = False
            while temp:
                digit = temp % 10
                cur.append(str(mapping[digit]))
                temp //= 10
                calculated = True
                
            
            if calculated:
                numsToVal[num] = int(''.join(cur[::-1]))
            else:
                numsToVal[num] = mapping[temp]
            numsToIdx[num] = i
            
        #print(numsToVal, numsToIdx)
        nums.sort(key = lambda x:(numsToVal[x], numsToIdx[x]))
        return nums