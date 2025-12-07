def convert_list(arr, toInt = False):
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
    0: [0, -1], #<
    1: [-1, 0], #^
    2: [0, 1],  #>
    3: [1, 0],  #v
}

from collections import defaultdict
from sortedcontainers import SortedList

c = SortedList()


with open('d5.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')
M = inputs.index('')
N = len(inputs)
for i in range(M):
    left, right = inputs[i].split('-')
    left = int(left)
    right = int(right)
    idx = c.bisect_left((left, right))
    #print(c, idx, left, right)
    while idx < len(c) and right >= c[idx][0]:
        right = max(right, c[idx][1])
        c.pop(idx)
    
    
    if idx > 0 and c[idx-1][1] >= left:
        left = min(left, c[idx-1][0])
        right = max(right, c[idx-1][1])
        c.pop(idx-1)
        
        
        
    
    c.add((left, right))
    #print(c, 'after')
p1 = 0
print(c)
for i in range(M+1, N):
    cur = int(inputs[i])
    
    i = c.bisect_left((cur, float('inf')))
    
    
    
    if i < len(c) and c[i][0] <= cur <= c[i][1]:    
        p1 += 1
    elif i-1 >= 0 and c[i-1][0] <= cur <= c[i-1][1]:
        p1 += 1
    

print(p1)


#980 too high p1
p2 = 0
for intervals in c:
    p2 += intervals[1] - intervals[0] + 1

print(p2)