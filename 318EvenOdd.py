n = [int(i) for i in input().split(" ")]

k = n[1]
n = n[0]
index = (n + 1) // 2

if k > index:  # in the even
    print(int(2 * (k - index)))
else:  # in the odd
    print(int(2 * k - 1))


# {1, 3, 5, 7, 9, 2, 4, 6, 8, 10}
# {1 3 5 7 2 4 6 8}
# when odd, it is 2n + 1 where n is the index
# when it is even after the index it is 2n.
