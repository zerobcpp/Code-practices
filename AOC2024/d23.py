import os
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


with open('d23.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')
graph = defaultdict(set)
for i in inputs:
    u, v = i.split('-')
    graph[u].add(v)
    graph[v].add(u)


possible = set()
seen = set()

password = set()
for p in graph:
    for neigh in graph[p]:
        temp = graph[p] & graph[neigh]
        password.add(tuple(sorted([i for i in temp] + [p, neigh])))
        for cand in temp:
            possible.add(tuple(sorted((p, neigh, cand))))

# print(possible)
print(len(possible))
p1 = 0
for i in possible:
    for j in i:
        if j.startswith('t'):
            p1 += 1
            break

print(p1)
# print(password)


def helper(s):
    s = list(s)
    n = len(s)
    # print(s, end = '\t')
    for i in range(n):
        for j in range(i+1, n):
            if s[j] not in graph[s[i]]:
                # print(s[j], s[i])
                return False

    return True


p2 = ''
for cand in password:
    if helper(cand):
        p2 = max(p2, cand, key=len)

print(','.join(p2))

