with open('d2.txt', 'r+') as f:
    inputs = f.read()

inputs = inputs.split('\n')

N = len(inputs)
#print(inputs)

p1 = 0
for i in inputs:
    nums = [int(i) for i in i.split()]
    N = len(nums)
    safe = True
    inc = False
    dec = False
    for j in range(N-1):
        if abs(nums[j] - nums[j+1]) > 3 or abs(nums[j] - nums[j+1]) < 1:
            safe = False
            break
        if nums[j] >= nums[j+1]:
            inc = True
        if nums[j] <= nums[j+1]:
            dec = True
    
    #print(nums, safe, inc, dec)
    if inc and dec:
        continue
    if safe:
        #print(nums)
        p1 += 1

print(p1)

def helper(nums):
    N = len(nums)
    inc = 0
    dec = 0
    for i in range(N-1):
        if 1 <= nums[i+1] - nums[i] <= 3:
            inc += 1
    
    for i in range(N-1):
        if 1 <= nums[i] - nums[i+1] <= 3:
            dec += 1
    return inc == N - 1 or dec == N-1

p2 = 0
for i in inputs:
    nums = [int(i) for i in i.split()]
    N = len(nums)

    for j in range(N):
        temp = nums[:j] + nums[j+1:]
        if helper(temp):
            p2 += 1
            break 

print(p2)




