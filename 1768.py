class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1 = False
        if len(word1) > len(word2):
            n = len(word2)
            s1 = True
        else:
            n = len(word1)
        res = []

        for i in range(n):
            res.extend([word1[i], word2[i]])

        if s1:
            res.extend(word1[i + 1:])
        else:
            res.extend(word2[i + 1:])

        return ''.join(res)

    def mergeAlternately(self, word1, word2):
        res = []
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                res.extend(word1[i])
            if i < len(word2):
                res.append(word2[i])

        return "".join(res)