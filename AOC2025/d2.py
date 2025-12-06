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
c = defaultdict()

with open('d2.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split(',')

res = 0

def part1():
    res = 0
    for i in range(l, r+1):
        cur = str(i)
        mid = len(cur) // 2
        if cur[:mid] == cur[mid:]:
            res += i 
    return res

def part2():
    res = 0
    for i in range(l, r+1):
        cur = str(i)
        N = len(cur)
        for j in range(N):
            if j == 0:
                parts = N
            else:
                parts = N // j
            if cur[:j] * parts == cur:
                res += i
                break
    
    
    '''
    cur = str(i)
    temp = 2 * cur
    return cur in temp[1:-1]
    #leetcode 459
    '''
            
    return res
            
for i in inputs:
    l, r = i.split('-')
    l = int(l)
    r = int(r)
    
    res += part2()
    


print(res)

