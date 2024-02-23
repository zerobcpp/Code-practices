class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" or needle == "":
            return 0
        for i in range(len(haystack)):
            count = 0
            for j in range(len(needle)):
                if i+j < len(haystack):
                    if needle[j] == haystack[i+j]:
                        count += 1
            if count >= len(needle):
                break
        if count == 0:
            return -1

        return i