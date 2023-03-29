class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']

        string = [i for i in s]

        while l < r:
            # print(l, r)
            if string[l] in vowels:
                while r > l:
                    if string[r] in vowels:
                        break
                    r -= 1
                string[l], string[r] = string[r], string[l]
                r -= 1
            l += 1


        return "".join(string)

if __name__ == '__main__':
    print(Solution().reverseVowels("leetcode"))

    s = "leetcode"
    l,r = 0, len(s) - 1
    print(s[l:])
    x = float('inf')
    if x > 0:
        x = 1
    print(x)
    c = [*s]
    x = (1,0)
    y = (-1,1)
    a,b = x
    print(a,b)