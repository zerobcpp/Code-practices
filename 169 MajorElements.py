import collections
def majorityelement(s):
    # s type = list[int]
    # return int

    count = 0
    candidate = None

    for num in s:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate



a = [1,1,1,1,1,2,3,4,5,6,7,7,7,8,8]
b = [-4,-4,-4,-4,1,2,3,4,1,2,3,4]
mins = min(b)
i = 0
while i<len(b):
    b[i] += abs(mins)
    i += 1

print(b)

print(majorityelement(a))