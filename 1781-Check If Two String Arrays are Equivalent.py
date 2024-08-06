class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s = ''.join(word1)
        s2 = ''.join(word2)
        
        return s == s2