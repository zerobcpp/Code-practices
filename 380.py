class RandomizedSet:

    def __init__(self):
        self.c = set()

    def insert(self, val: int) -> bool:
        if val not in self.c:
            self.c.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        try: 
            self.c.remove(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
        return choice(list(self.c))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()