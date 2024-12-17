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


with open('d17.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')

instrs = list(int(i) for i in inputs[4][9:].split(','))


ptr = 0
N = len(instrs)


def p1():
    A = int(inputs[0][11:])
    B = int(inputs[1][11:])
    C = int(inputs[2][11:])

    def choose(val):

        match val:
            case 4:
                return A
            case 5:
                return B
            case 6:
                return C
            case _:
                return val

    i = 0
    out = []
    while i < N:
        op, val = instrs[i], instrs[i+1]
        this = None

        match op:
            case 0:
                A //= (2 ** choose(val))
            case 1:
                B ^= val
            case 2:
                B = choose(val) % 8
            case 3:
                if A != 0:
                    i = val
                    continue
            case 4:
                B ^= C
            case 5:
                out.append(choose(val) % 8)
            case 6:
                B = A // (2 ** choose(val))
            case 7:
                C = A // (2 ** choose(val))

        print(i, op, [A, B, C], out)
        i += 2

    # wanted = out
    print(','.join([str(i) for i in out]))
    # print(out)

# 2,2,1,0,7,3,2,1,1 wrong
# 7,3,0,5,7,1,4,0,5 correct


def p2():
    def helper(j):
        nonlocal best
        A = j
        B = 0
        C = 0

        def choose(val):
            match val:
                case 4:
                    return A
                case 5:
                    return B
                case 6:
                    return C
                case 7:
                    assert False
                case _:
                    return val

        i = 0
        out = []

        while i < N:

            op, val = instrs[i], instrs[i+1]

            match op:
                case 0:
                    A //= (2 ** choose(val))
                case 1:
                    B ^= val
                case 2:
                    B = choose(val) % 8
                case 3:
                    if A != 0:
                        i = val
                        continue
                case 4:
                    B ^= C
                case 5:
                    out.append(choose(val) % 8)
                    n = len(out)
                    if n < N and out[n-1] != instrs[n-1]:
                        return out
                case 6:
                    B = A // (2 ** choose(val))
                case 7:
                    C = A // (2 ** choose(val))

            i += 2
            # print(i, op, [A, B, C], out)

        return out

    cur = 0
    best = 0
    print(f'desired output: {instrs=}')
    while True:
        itr = cur * (8 ** 10) + 0o4432025052
        arr = helper(itr)

        if arr == instrs:
            print(itr, arr)
            break
        # print(arr, itr)
        if len(arr) > best:
            best = len(arr)
            print(arr, oct(itr), itr)
        cur += 1


# p1()

p2()
