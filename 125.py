class Solution:
    def isPalindrome(self, s: str) -> bool:
        fix = [i.lower() for i in s if i.isalpha()]
        return fix == fix[::-1]
        