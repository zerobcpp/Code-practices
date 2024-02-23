class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(list(words[0]))
        words.pop(0)
        for i in words:
            c1 = Counter(list(i))
            update = list((c&c1).elements())
        return update
        
