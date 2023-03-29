class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s = []
        res = []
        def helper(open, close):
            if open == close and open == n:
                res.append("".join(s))
                return

            if open < n:
                s.append('(')
                helper(open + 1, close)
                s.pop()
            if close < open:
                s.append(')')
                helper(open, close+1)
                s.pop()

        helper(0, 0)
        return res


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
