class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join(map(str,digits))
        num = int(num)+1
        digits = [int(i) for i in str(num)]
        return digits