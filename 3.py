class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        for i in s:
            if i in seen:
                break
            seen.add(i)
        return len(seen)