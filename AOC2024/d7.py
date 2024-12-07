def helper(arr, res, N):
    cache = {}
    def recur(i, cur):
        if i >= N:
            if cur == res:
                return res
            return 0
        if (i, cur) in cache:
            return cache[i, cur]
    
        mul = recur(i+1, cur * arr[i])
        add = recur(i+1, cur + arr[i])

        # p2
        strs = recur(i + 1, int(str(cur) + str(arr[i])))
        #

        cache[i, cur] = any([mul, add, strs])

        return cache[i, cur]
    
    return recur(1, arr[0])



def loop(lines):
    result, arr = lines.split(':')
    arr = arr[1:].split()
    arr = [int(i) for i in arr]
    result = int(result)
    N = len(arr)

    
    if(helper(arr, result, N)):
        return result
    
    return 0




if __name__ == '__main__':
    import time
    import multiprocessing
    with open('d7.txt', 'r+') as f:
        inputs = f.read()
    inputs = inputs.split('\n')

    b = time.time()
    with multiprocessing.Pool(1) as pool:
        # Map each line of input to a process for processing
        results = pool.map(loop, inputs)

    # Summing up all the results from the processes
    p1 = sum(results)
    print(p1)
    a = time.time()
    print(a - b)
    




#print(p1)
#3119088655389
#264184041398847

#264184041398847
#17.117719650268555


#ints = 1.082723617553711
#eval = 17.117719650268555