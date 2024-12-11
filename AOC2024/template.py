def convert_list(arr, toInt = False):
    N = len(arr)
    for i in range(N):
        if toInt:
            arr[i] = [int(j) for j in inputs[i]]
        else:
            arr[i] = list(arr[i])
    return arr

dist4 = [0, -1, 0, 1, 0]


with open('d.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')

