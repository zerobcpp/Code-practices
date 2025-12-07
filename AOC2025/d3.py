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

with open('d3.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')
p1 = p2 = 0
for i in inputs:
    seen = set()
    mx = -1
    remove = len(i) - 12
    for j in i[::-1]:
        
        for k in seen:
            poss = j + k
            mx = max(mx, int(poss))
        
        seen.add(j)
    
    p1 += mx
    st = []
    
    for j in i:
        while remove and st and st[-1] < j:
            st.pop()
            remove -= 1
        st.append(j)
    #print(len(st), st)
    p2 += int(''.join(st[:12]))
# p1 = hashmap question
# p2 = monotonic stack
print(p1, p2)
    

