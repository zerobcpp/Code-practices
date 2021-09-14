s = input()

sset = {i for i in s}


if 'H' in sset or 'Q' in sset or '9' in sset:
    print("YES")
else:
    print("NO")
