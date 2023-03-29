class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = [0] * 27
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

    def lengthOfLongestSubver2(self, s):
        char = [0] * 127
        lf = rt = 0
        smap = [ord(i) - ord('a') for i in s]
        print(smap)
        return 0

if __name__ == '__main__':
    print(Solution.lengthOfLongestSubstring(self = None, s = "abcabcbb"))
    print(Solution.lengthOfLongestSubver2(self=None, s="abcabcbb"))

