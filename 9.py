class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = [i for i in str(x)]
        #print(res)
        return res == res[::-1]