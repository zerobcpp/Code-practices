from collections import Counter
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        c = Counter(list(words[0]))
        words.pop(0)
        for i in words:
            c1 = Counter(list(i))
            c &= c1
        #print(update)
        return list(c.elements())



if __name__ == "__main__":
    a = Solution.commonChars(None, ["bella","label","roller"])
    print(a)