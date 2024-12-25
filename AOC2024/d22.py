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
from itertools import product
c = defaultdict()

with open('d22.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')


#SECRET = 64 / 32 * 2048
MOD = 16777216

p1 = 0

SEQ = defaultdict(int)

def can(change, price):
    N = len(change)
    c = {}
    for i in range(N-3):
        k = (change[i], change[i+1], change[i+2], change[i+3])
        c[k] = c.get(k, price[i+4])
        c[k] = max(c[k], price[i+4])
    
    return c
    
    
    
for i in inputs:
    start = int(i)
    price = []
    change = []
    for i in range(2000):
        price.append(start % 10)
        start ^= (start * 64)
        
        start %= MOD
        
        start ^= (start // 32)
        
        start ^= (start * 2048)
        start %= MOD
    p1 += start
    
    for i in range(1, len(price)):
        change.append(price[i] - price[i-1])
    
    c = can(change, price)
    for i, v in c.items():
        SEQ[i] += v


print(p1)
print(max(SEQ.values()))

