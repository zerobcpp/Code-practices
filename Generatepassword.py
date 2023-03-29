def generate(length):
    res = []
    def helper(idx, remaining, arr):
        if remaining == 0:
            res.append(arr[:])
            return

        for i in range(idx, 122):
            arr.append(chr(i))
            helper(i+1, remaining-1, arr)
            arr.pop()

    helper(65, length, [])
    print(res)
    print(len(res))
    return res

generate(2)