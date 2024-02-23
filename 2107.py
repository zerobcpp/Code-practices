class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nb = len(nums[0])
        combination = set(int(i, 2) for i in nums)
        # print(combination)
        for i in range(pow(2, n) - 1, 0, -1):
            if i not in combination:
                return f'{i:0{nb}b}'
        return "0"*nb 
    
    
    def findDifferentBinaryString(self, nums):
        N = len(nums)
        NB = len(nums[0])
        c = set()
        
        def helper(i, arr):
            if i == NB:
                c.add(''.join(arr))
                return 
            
            arr.append('0')
            helper(i+1, arr)
            arr.pop()
            arr.append('1')
            helper(i+1, arr)
            arr.pop()
            
        nums = set(nums)
        helper(0, [])
        for i in c:
            if i not in nums:
                return i
            
            
        return -1
        

            
            