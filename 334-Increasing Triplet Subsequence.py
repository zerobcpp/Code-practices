class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        one = two = inf
        
        for i in nums:
            if i > two:
                return True
            if i <= one:
                one = i
            else:
                two = i
        return False