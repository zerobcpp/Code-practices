class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        nums = "".join(map(str,num))
        total = int(nums) + k
        total = str(total)
        return [i for i in total]