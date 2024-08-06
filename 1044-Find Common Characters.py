class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(list(words[-1]))
        words.pop()
        for i in words:
            c1 = Counter(list(i))
            c &= c1
        return list(c.elements())
        
