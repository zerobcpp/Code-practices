from functools import cache
from collections import defaultdict


def convert_list(arr, toInt=False):
    N = len(arr)
    for i in range(N):
        if toInt:
            arr[i] = [int(j) for j in inputs[i]]
        else:
            arr[i] = list(arr[i])
    return arr


def d8(x, y):
    cords = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i or j:
                cords.append((x+i, y+j))
    return cords


d4 = [0, -1, 0, 1, 0]
dr = {
    0: [0, -1],  # <
    1: [-1, 0],  # ^
    2: [0, 1],  # >
    3: [1, 0],  # v
}

with open('d19.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')


p = 0
words = []
req = []
for i in inputs:
    if i == '':
        p = 1
        continue
    if p == 0:
        words.append(i)
    elif p == 1:
        req.append(i)

words = words[0].split(', ')


words = set(words)


c = defaultdict(int)


def p1():
    def helper(s, i, N):

        if i >= N:
            return True

        for w in words:
            n = len(w)

            if s[i:i+n] == w:
                if helper(s, i+n, N):
                    return True

        return False

    p1 = 0
    for i in req:

        N = len(i)
        p1 += helper(i, 0, N)
    print(p1)


def p2():
    c = defaultdict(int)
    cache = {}

    def helper(s, i, N):
        if i >= N:
            return 1
        if (s, i) in cache:
            return cache[s, i]
        ways = 0
        for w in words:
            n = len(w)
            if s[i:i+n] == w:
                ways += helper(s, i+n, N)

        cache[s] = ways
        return ways

    p2 = 0
    for i in req:
        n = len(i)
        print(i)
        p2 += helper(i, 0, n)

    print(p2)


p2()
