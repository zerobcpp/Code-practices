# 28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        for i in range(h - n + 1):
            if haystack[i : i+n] == needle:
                return i
        return -1
    
    def strStr(self, hay, needle):
        h = len(hay)
        n = len(needle)
        
        for i in range(h - n + 1):
            found = True
            for j in range(n):
                if hay[i+j] != needle[j]:
                    found = False
                    break
            if found:
                return i
        
        return -1
                    
                    