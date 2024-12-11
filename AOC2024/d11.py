def convert_list(arr, toInt = False):
    N = len(arr)
    for i in range(N):
        if toInt:
            arr[i] = [int(j) for j in inputs[i]]
        else:
            arr[i] = list(arr[i])
    return arr

dist4 = [0, -1, 0, 1, 0]


with open('d11.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split()
N = len(inputs)
#print(inputs)

def p1():
    K = 0 # p1
    cur = inputs
    while K > 0:
        temp = []
        for i in cur:
            
            if int(i) == 0:
                temp.append(str(int(i)+1))
            elif len(i) % 2 == 0:
                mid = len(i) // 2
                temp.append(str(int(i[:mid])))
                temp.append(str(int(i[mid:])))
            else:
                temp.append(str(int(i) * 2024))
        
        cur = temp
        #print(cur)
        K -= 1
        print(K)

    print(len(cur))


from collections import defaultdict


def convert(stone):
    if stone == '0':
        return ['1']
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        temp = []
        temp.append(str(int(stone[:mid])))
        temp.append(str(int(stone[mid:])))
        return temp
    else:
        return [str(int(stone) * 2024)]

        

    
c  = defaultdict(int)
for i in inputs:
    c[i] += 1

#print(c)
# can be use for p1.
for i in range(75):
    new_c = defaultdict(int)

    for k, v in c.items():
        count = convert(k)
        for x in count:
            new_c[x] += v
        
    #print(c)
    c = new_c

#print(c)
print(len(c.keys()))
print(sum(c.values()))


        



