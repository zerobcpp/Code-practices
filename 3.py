class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char = [0] * 127
        left = right = 0
        count = 0
        for i in range(len(s)):
            rcptr = ord(s[right]) - ord('a')
            char[rcptr] += 1
            while char[rcptr] > 1:
                lcptr = ord(s[left]) - ord('a')
                char[lcptr] -= 1
                left += 1
            count = max(count, (right-left)+1)
            right += 1
        return count