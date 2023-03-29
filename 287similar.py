from collections import Counter
def findDuplicate(nums):
    slow, fast = nums[0], nums[0]
    while True:
        slow, fast = nums[slow], nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow, fast = nums[slow], nums[fast]
    return slow


def findDuplicate2(nums):
    beg, end = 1, len(nums) - 1

    while beg + 1 <= end:
        mid, count = (beg + end) // 2, 0
        for num in nums:
            if num <= mid: count += 1
        if count <= mid:
            beg = mid + 1
        else:
            end = mid
    return end


def singleNum(nums):
    res = 0
    for i in nums:
        res ^= i
    return res

def singleNumDict(nums):
    count = dict(dict.fromkeys(nums, 0))
    print(count)
    for i in nums:
        count[i] += 1

    for i, j in count.items():
        if count[i] == 1:
            return i

if __name__ == "__main__":
    print(findDuplicate([6, 2, 4, 1, 3, 7, 5, 2]))
    print(singleNumDict([4, 2, 4, 2, 5]))

    a = ["bella","label","roller"]
    c = set(list(a[0]))
    for i in range(1,len(a)):
        c.intersection_update(a[i])
    print(c)