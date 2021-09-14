usrname = [i for i in input()]
usrset = {i for i in usrname}

if len(usrset) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")