# Problem, given some string, 001? or 00??
# return these values
# 1st example: 0011 and 0010
# 2nd example: 0011 0010 0000 0001


def generate(s):
    n = len(s)
    res = []
    def helper(idx, arr):
        if len(arr) == n:
            res.append("".join(arr))
            return
        if s[idx] == '?':
            helper(idx+1, arr + ['1'])
            helper(idx+1, arr + ['0'])
        else:
            helper(idx+1, arr + [s[idx]])

    helper(0, [])
    return res


print(generate('00??'))


