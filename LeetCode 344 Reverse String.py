def ReverseString(self, s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    #Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
    """

    end = len(s) - 1
    resultwhile = list()
    resultfor = list()

    while end >= 0:
        resultwhile.append(s[end])
        end -= 1
    for i in s[::-1]:
        resultfor.append(i)

    i = 0
    end = len(s) - 1
    while end >= len(s) // 2:
        strlist = list(s)
        strlist[i], strlist[end] = strlist[end], strlist[i]
        s = "".join(strlist)
        i += 1
        end -= 1

    print(s)
    print(resultfor)
    print(resultwhile)
    s = s[::-1]
    s = s[::-1]
    print(s)
    return s


a = ReverseString(self=None, s="Hesllo")
print(a)
