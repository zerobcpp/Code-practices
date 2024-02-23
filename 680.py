class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # create two possible choice
                s1 = s[l:r]
                s2 = s[l+1:r+1]
                
                return s1 == s1[::-1] or s2 == s2[::-1]
            l += 1
            r -= 1
        return True
                