class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i, j in zip(word1, word2):
            res.extend([i,j])
        
        return ''.join(res)