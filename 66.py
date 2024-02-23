class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits)-1
        digits[idx] = digits[idx] + 1
        return digits