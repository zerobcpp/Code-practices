class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        idx = len(self.list)
        self.map[val] = idx
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        idx = self.map[val]
        swap = self.list[-1]
        self.list[idx] = swap
        self.map[swap] = idx
        self.list.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        rand = randint(0, len(self.list)-1)
        return self.list[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()