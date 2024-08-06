class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        c = defaultdict(int)
        for i in words:
            c[tuple(sorted(i))] += 1
            
        res = 0
        for i, v in c.items():
            res += v // 2
        
        return res
        