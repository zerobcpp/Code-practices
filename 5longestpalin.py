class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        sol = []
        n = len(s)
        for i in range(n):
            for add in range(2):
                left = i
                right = i + add
                while left >= 0 and right < n and s[left] == s[right]:
                    if right - left + 1 > length:
                        length = right - left + 1
                        sol = s[left:right+1]
                    left -= 1
                    right += 1
        return sol


if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("babad"))
