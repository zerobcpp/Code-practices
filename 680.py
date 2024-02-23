class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = [i for i in s]
        l, r = 0, len(string) - 1
        mid = l + (r-l) // 2
        delete = True
        while l < mid:
            #print(l,r)
            if string[l] == string[r]:
                l += 1
                r -= 1
            if string[l] != string[r]:
                string[r] = string[r-1]
                string.pop(r)
                break
        print(string)
        return string[::] == string[::-1]