class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if i not in t:
                return False
        
        return True