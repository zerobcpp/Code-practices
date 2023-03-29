def findDifferentBinaryString(nums: list[str]) -> str:
    n = len(nums)
    combination = set(int(i, 2) for i in nums)
    # print(combination)
    for i in range(pow(2, n) - 1, 0, -1):
        if i not in combination:
            return format(i, 'b')


if __name__ == '__main__':
    print(findDifferentBinaryString(["111","011","001"]))
    a = [6,3,1,3,6]
    print(a==a[::-1])
