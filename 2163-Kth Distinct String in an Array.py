class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        cur = 0
        for i, v in c.items():
            if v == 1:
                cur += 1
                if cur == k:
                    return i
        
        return ''