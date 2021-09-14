# can also use sets, but make sure to minus the 0 from the set
# so it doesn't affect the final result
level = int(input())
pass1 = [int(i) for i in input().split(" ")]
pass2 = [int(i) for i in input().split(" ")]

levelcheck = [None] * (level + 1)
levelcheck[0] = True
for i in pass1:
    levelcheck[i] = True
for i in pass2:
    levelcheck[i] = True

if not any(levelcheck):
    print("Oh, my keyboard!")
else:
    print("I become the guy.")
